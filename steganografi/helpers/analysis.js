import { statSync } from 'fs';

const inputFile = "../image.jpeg";
const outputFile = "../hidden.jpeg";

const statsInput = statSync(inputFile);
const statsOutput = statSync(outputFile);

console.log(`Orijinal Dosya boyutu: ${statsInput.size / 1024} kilobyte\n`);
console.log(`Yeni Dosya boyutu: ${statsOutput.size / 1024} kilobyte\n`); 