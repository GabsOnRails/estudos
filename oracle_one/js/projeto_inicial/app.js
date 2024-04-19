alert('Boas vindas ao jogo do número secreto!');
let numeroMaximo = 10000;
let numeroSecreto = parseInt(Math.random() *numeroMaximo +1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);
    if (chute == numeroSecreto) {
        break;
    }
    else {
        if(chute > numeroSecreto) {
            alert(`O número secreto é menor que ${chute}`);  
        }
        else {
            alert(`O número secreto é maior que ${chute}`);
        }
        tentativas ++
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Acertou, miseraví! O número era ${numeroSecreto} e você fez ${tentativas} ${palavraTentativa}.`);

// if (tentativas > 1) {
//     alert(`Acertou, miseraví! O número era ${numeroSecreto} e você fez ${tentativas} tentativas.`);
// }
// else {
//     alert(`Acertou, miseraví! O número era ${numeroSecreto} e você fez ${tentativas} tentativa.`);
// }

