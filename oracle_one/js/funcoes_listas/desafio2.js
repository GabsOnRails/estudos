
// Criar uma função que exibe "Olá, mundo!" no console.
function olaMundo() {
    console.log('olá,mundo!');
}

// Criar uma função que recebe um nome como parâmetro e exibe "Olá, [nome]!" no console.
function olaNome(nome){
    console.log(`Olá,${nome}`);
}
olaNome('Gabriel');

// Criar uma função que recebe um número como parâmetro e retorna o dobro desse número.
function numeroDobrado(numero){
    return numero * 2;
}
console.log(numeroDobrado(4));

// Criar uma função que recebe três números como parâmetros e retorna a média deles.
function calcularMedia(num1,num2,num3) {
    return (num1 + num2 + num3) / 3;
}

let media=calcularMedia(4,7,12);
console.log(media);

// Criar uma função que recebe dois números como parâmetros e retorna o maior deles.
function retornaMaiorNumero(retorno1,retorno2) {
    return retorno1 > retorno2 ? retorno1 : retorno2;
}
let maiorNumero = retornaMaiorNumero(8,4);
console.log(maiorNumero);
// Criar uma função que recebe um número como parâmetro e retorna o resultado da multiplicação desse número por ele mesmo
function multiplicaPorEleMesmo(numeroMultiplicado) {
    return numeroMultiplicado * numeroMultiplicado; 
}
let resultado = multiplicaPorEleMesmo(4);
console.log(resultado);
    










