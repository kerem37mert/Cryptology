import { readFileSync, writeFileSync } from 'fs';

const messageToBits = (message) => {
    return message.split('').map(char => {
        return char.charCodeAt(0).toString(2).padStart(8, '0');
    }).join('');
}

const bitsToMessage = (bits) => {
    const chars = [];

    for (let i = 0; i < bits.length; i += 8) 
        chars.push(String.fromCharCode(parseInt(bits.slice(i, i + 8), 2)));
    
    return chars.join('');
}

const hideMessage = (inputWav, outputWav, message) => {
    const data = readFileSync(inputWav);
    const header = data.slice(0, 44); // WAV header
    const body = Buffer.from(data.slice(44)); // Audio data

    message += '###';
    const bits = messageToBits(message);

    if (bits.length > body.length)
        throw new Error("Mesaj çok uzun, ses dosyasına sığmıyor.");

    for (let i = 0; i < bits.length; i++) 
        body[i] = (body[i] & 0b11111110) | parseInt(bits[i]);

    const output = Buffer.concat([header, body]);
    writeFileSync(outputWav, output);
    console.log("Mesaj başarıyla gizlendi.");
}


const revealMessage = (inputWav) => {
    const data = readFileSync(inputWav);
    const body = data.slice(44); // Skip header

    let bits = '';

    for (let i = 0; i < body.length; i++)
        bits += (body[i] & 1).toString();

    const message = bitsToMessage(bits);
    return message.split('###')[0];
}


const wavFile = "sound.wav";
const hiddenWavFile = "hidden.Wav";
const message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pellentesque odio et fringilla vestibulum. Duis vehicula, nulla sed commodo vestibulum, mi cras."

// Mesajı Gizle
hideMessage(wavFile, hiddenWavFile, message);
console.log(`${wavFile} ses dosyasına \n "${message}" \n mesajı gizlenerek ${hiddenWavFile} isimli yeni ses dosyası oluşturuldu`);

console.log("\n");

// Mesajı Görüntüle
const hiddenMessage = revealMessage(hiddenWavFile);
console.log(`${hiddenWavFile} içerisinde yer alan gizli mesaj: \n${hiddenMessage}`);