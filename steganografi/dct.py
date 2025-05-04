import cv2
import numpy as np

def message_to_bits(message):
    """Mesajı bit dizisine çevirir."""
    return ''.join([format(ord(c), '08b') for c in message])

def bits_to_message(bits):
    """Bit dizisini mesaja çevirir."""
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join([chr(int(b, 2)) for b in chars])

def hide_message(image_path, output_path, message):
    """Mesajı görüntüye gizler."""
    img = cv2.imread(image_path)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # YCbCr renk uzayına dönüştür
    y, cr, cb = cv2.split(ycrcb)  # Y (ışık), Cr ve Cb kanallarını ayır

    h, w = y.shape  # Görüntü boyutları

    message += '###'  # Sonlandırıcı ekle
    bits = message_to_bits(message)  # Mesajı bit dizisine çevir
    bit_idx = 0

    y_new = y.copy()  # Y kanalını kopyala

    # Görüntüyü 8x8 bloklara ayır
    for row in range(0, h, 8):
        for col in range(0, w, 8):
            block = y[row:row+8, col:col+8]
            if block.shape != (8, 8):  # 8x8 boyutunda olmayan blokları geç
                continue

            dct_block = cv2.dct(np.float32(block))  # DCT dönüşümünü yap
            flat = dct_block.flatten()  # Bloğu düzleştir

            # İlk DCT koeffisientini değiştir
            if bit_idx < len(bits):
                coeff = int(flat[0])  # İlk koeffisienti al
                coeff = (coeff & ~1) | int(bits[bit_idx])  # En düşük biti değiştir
                flat[0] = coeff  # Güncellenmiş koeffisienti bloğa yaz
                bit_idx += 1

            # IDCT dönüşümü yap ve bloğu yeniden yaz
            dct_block = flat.reshape((8, 8))
            idct_block = cv2.idct(np.float32(dct_block))
            y_new[row:row+8, col:col+8] = np.uint8(np.clip(idct_block, 0, 255))

            if bit_idx >= len(bits):
                break
        if bit_idx >= len(bits):
            break

    # Y kanalını güncelle ve renkli görüntüyü geri oluştur
    merged = cv2.merge([y_new, cr, cb])
    color_img = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
    cv2.imwrite(output_path, color_img)

    print("Mesaj başarıyla gizlendi.")

def reveal_message(image_path):
    """Mesajı görüntüden çıkar."""
    img = cv2.imread(image_path)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # YCbCr renk uzayına dönüştür
    y, cr, cb = cv2.split(ycrcb)  # Y (ışık), Cr ve Cb kanallarını ayır

    h, w = y.shape
    bits = ''

    # Görüntüyü 8x8 bloklara ayır
    for row in range(0, h, 8):
        for col in range(0, w, 8):
            block = y[row:row+8, col:col+8]
            if block.shape != (8, 8):  # 8x8 boyutunda olmayan blokları geç
                continue

            dct_block = cv2.dct(np.float32(block))  # DCT dönüşümünü yap
            flat = dct_block.flatten()  # Bloğu düzleştir

            # İlk DCT koeffisientinin en düşük bitini al
            bits += str(int(flat[0]) & 1)

            message = bits_to_message(bits)
            if '###' in message:  # Sonlandırıcıyı bul
                return message.split('###')[0]  # Mesajı döndür

    return ""  

input_file = "image.jpeg"
output_file = "hidden.jpeg"
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pellentesque odio et fringilla vestibulum. Duis vehicula, nulla sed commodo vestibulum, mi cras."

# Mesajı gizle
hide_message(input_file, output_file, message)
print(f'{input_file} adlı dosyaya \n"{message}"\nmesajı gizlenerek {output_file} oluşturuldu')

# Mesajı oku
print("Gizli mesaj:", reveal_message(output_file))
