import { statSync } from 'fs';

const inputFile = "../sound.wav";
const outputFile = "../hidden.wav";

const statsInput = statSync(inputFile);
const statsOutput = statSync(outputFile);

console.log(`Orijinal Dosya boyutu: ${statsInput.size / 1024} kilobyte\n`);
console.log(`Yeni Dosya boyutu: ${statsOutput.size / 1024} kilobyte\n`); 