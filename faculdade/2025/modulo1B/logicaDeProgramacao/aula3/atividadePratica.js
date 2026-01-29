//Escreva um algoritmo que:
// some três números;
// Calcule a média entre três números;
// Mostre o resultado na tela da soma e da média calculada.

//--------------------------------------------------------------------//

//Var declaration

let numero1 = 5;
let numero2 = 6.4;
let numero3 = 4.6;
let soma = numero1 + numero2 + numero3;
let media = soma / 3;

console.log(`A soma das notas é: ${soma}\nA média é de: ` + Math.trunc(media));
