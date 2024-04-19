// Desafios

// Crie um contador que comece em 1 e vá até 10 usando um loop while. Mostre cada número.
//Crie um contador que começa em 10 e vá até 0 usando um loop while. Mostre cada número.
//Crie um programa de contagem regressiva. Peça um número e conte deste número até 0, usando um loop while no console do navegador.
//Crie um programa de contagem progressiva. Peça um número e conte de 0 até esse número, usando um loop while no console do navegador.

// contar 1 até o 10
let inicial = 1;
let final = 10;

while(inicial!=final) {
    alert(`A contagem está em ${inicial}`)
    inicial++;
}

// contar de 10 até 1
let inicial1 = 10;
let final1 = 1;

while(inicial!=final1) {
    alert(`A contagem está em ${inicial1}`)
    inicial1--;
}

// contagem regressiva
let final2 = 0
let inicial2 = prompt('Qual o número inicial?')
while(inicial2!=final2) {
    alert(`A contagem está em ${inicial2}`)
    inicial2--;
}

// contagem progessiva
let final3 = prompt('Qual o número final?')
let inicial3 = 0
while(inicial3!=final3) {
    alert(`A contagem está em ${inicial3}`)
    inicial3++;
}