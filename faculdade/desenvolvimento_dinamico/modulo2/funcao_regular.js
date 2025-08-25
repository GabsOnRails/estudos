//definindo uma função regular com dois parâmetros
function soma(a, b) {
  return a + b;
}
//chamando a função e armazenando o resultado em uma variável
let resultado = soma(2, 5);
console.log("o resultado da função soma é: " + resultado); //exibindo o resultado da função
console.log("o resultado da função soma é: " + soma(8, 2));
//Definindo uma função regular usando a palavra-chave function
function saudacao(nome) {
  console.log("olá, " + nome + ". Tudo bem?");
}
//chmando a função saudacao e passando um argumento
saudacao("Jorge");
//defindo uma função regular sem parâmetros e sem retorno
function mensagem() {
  console.log("Esta é uma mensagem de boas vindas");
}
//chamando a função mensagem
mensagem();
saudacao("Ana");
