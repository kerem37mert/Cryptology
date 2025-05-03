import { statSync } from 'fs';

const inputFile = "../sound.wav";
const outputFile = "../hidden.wav";

const statsInput = statSync(inputFile);
const statsOutput = statSync(outputFile);

console.log(`Orijinial Dosya boyutu: ${statsInput.size / 1024} kilobyte\n`);
console.log(`Orijinial Dosya boyutu: ${statsOutput.size / 1024} kilobyte\n`);