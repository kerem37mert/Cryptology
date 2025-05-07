import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, ifft

def hide_message_in_audio(audio_path, message, output_path):
    rate, data = wavfile.read(audio_path)
    
    if data.ndim > 1:
        data = data[:, 0]  # Mono kanal
    
    # Mesajı bit dizisine çevir
    bits = ''.join(format(ord(char), '08b') for char in message)
    
    data = data.astype(float)
    transformed = fft(data)

    start_idx = len(transformed) - len(bits) - 1000  # Son kısmı kullanıyoruz
    amplitude = 50  # Gömme kuvveti

    for i, bit in enumerate(bits):
        idx = start_idx + i
        if bit == '1':
            transformed[idx] += amplitude
        else:
            transformed[idx] -= amplitude

    modified_data = np.real(ifft(transformed)).astype(np.int16)
    wavfile.write(output_path, rate, modified_data)

def extract_message_from_audio(audio_path, message_length, amplitude=50):
    rate, data = wavfile.read(audio_path)
    if data.ndim > 1:
        data = data[:, 0]

    transformed = fft(data.astype(float))
    start_idx = len(transformed) - (message_length * 8) - 1000

    bits = ''
    for i in range(message_length * 8):
        idx = start_idx + i
        val = transformed[idx].real

        # Karar mekanizması: 0'a göre mi daha büyük, küçük mü?
        if val >= 0:
            bits += '1'
        else:
            bits += '0'

    # Bit dizisini ASCII'ye çevir
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        try:
            char = chr(int(byte, 2))
            # ASCII filtresi (bozulmuş karakterleri ayıklar)
            if 32 <= ord(char) <= 126:
                chars.append(char)
            else:
                chars.append(' ')
        except:
            chars.append(' ')
    
    return ''.join(chars)

# Kullanım
input_file = "sound.wav"
output_file = "hidden.wav"

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pellentesque odio et fringilla vestibulum. Duis vehicula, nulla sed commodo vestibulum, mi cras."

# Mesajı gizle
hide_message_in_audio(input_file, message, output_file)
print(f'{input_file} adlı dosyaya mesaj gizlendi ve {output_file} olarak kaydedildi.')

# Mesajı çöz
decoded_message = extract_message_from_audio(output_file, 160)
print("Gizli mesaj:", decoded_message)
