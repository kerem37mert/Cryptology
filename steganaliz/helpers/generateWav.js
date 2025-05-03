import { writeFileSync } from 'fs';

const generateChordWav = (filename, duration = 10, sampleRate = 44100) => {
    const freqs = [440, 523, 659]; // A, C, E notaları
    const numSamples = duration * sampleRate;
    const data = [];

    for (let i = 0; i < numSamples; i++) {
        let t = i / sampleRate;
        let sample = freqs.reduce((sum, f) => sum + Math.sin(2 * Math.PI * f * t), 0);
        sample = Math.round(32767 * sample / freqs.length); // normalize
        data.push(sample & 0xff);         // low byte
        data.push((sample >> 8) & 0xff);  // high byte
    }

    const byteRate = sampleRate * 2;
    const blockAlign = 2;
    const subchunk2Size = data.length;
    const chunkSize = 36 + subchunk2Size;

    const header = Buffer.alloc(44);
    header.write('RIFF', 0);
    header.writeUInt32LE(chunkSize, 4);
    header.write('WAVE', 8);
    header.write('fmt ', 12);
    header.writeUInt32LE(16, 16);
    header.writeUInt16LE(1, 20);
    header.writeUInt16LE(1, 22);
    header.writeUInt32LE(sampleRate, 24);
    header.writeUInt32LE(byteRate, 28);
    header.writeUInt16LE(blockAlign, 32);
    header.writeUInt16LE(16, 34);
    header.write('data', 36);
    header.writeUInt32LE(subchunk2Size, 40);

    const wavBuffer = Buffer.concat([header, Buffer.from(data)]);
    writeFileSync(filename, wavBuffer);

    console.log(`Oluşturuldu: ${filename}`);
}

generateChordWav('../sound.wav');