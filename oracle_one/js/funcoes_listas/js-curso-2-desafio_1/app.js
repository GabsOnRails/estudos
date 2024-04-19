let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do desafio';

function exibirMensagemConsole() {
    console.log('o botão foi clicado!');
}

function exibirAlerta() {
    alert('Eu amo JS');
}

function exibirPrompt() {
    let cidadeBrasil = prompt('Digite uma cidade do Brasil que você gosta muito:');
    alert(`Estive em ${cidadeBrasil} e lembrei de você!`);
}

function soma() {
    let numero1 = parseInt(prompt('Digite o primeiro número da soma:'));
    let numero2 = parseInt(prompt('Digite o segundo número para somar:'));
    let resultado = numero1 + numero2
    alert(`O resultado da soma ${numero1} + ${numero2} é ${resultado}`);
}
