import numpy as np
from scipy.io import wavfile

MAX_MSG_LENGTH = 160  # karakter

def message_to_bits(message):
    message = message.ljust(MAX_MSG_LENGTH)  # 160 karaktere sabitle
    return ''.join(format(ord(c), '08b') for c in message)

def bits_to_message(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars).strip()

def hideMessage(input_wav, output_wav, message):
    # WAV dosyasını oku
    rate, data = wavfile.read(input_wav)

    # Tek kanallı hale getir (mono) ya da sadece bir kanalı kullan
    if data.ndim > 1:
        data = data[:, 0]

    flat_data = data.copy()

    # Mesajı bit dizisine çevir
    bits = message_to_bits(message)

    if len(bits) > len(flat_data):
        raise ValueError("Ses dosyası mesajı saklamak için yeterince büyük değil.")

    # Mesajı LSB'ye göm
    for i, bit in enumerate(bits):
        flat_data[i] = (flat_data[i] & ~1) | int(bit)

    wavfile.write(output_wav, rate, flat_data.astype(data.dtype))
    print("Mesaj başarıyla gizlendi:", message, "\n")

def revealMessage(stego_wav):
    rate, data = wavfile.read(stego_wav)

    if data.ndim > 1:
        data = data[:, 0]

    bits = ''.join(str(sample & 1) for sample in data[:MAX_MSG_LENGTH * 8])
    message = bits_to_message(bits)
    print("Çözülen mesaj:", message)
    return message

wavFile = "sound.wav"
hiddenWavFile = "hidden_bpcs.Wav"
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pellentesque odio et fringilla vestibulum. Duis vehicula, nulla sed commodo vestibulum, mi cras."

hideMessage(wavFile, hiddenWavFile, message)
revealMessage(hiddenWavFile)
