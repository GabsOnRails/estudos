//!Arrow functions
//----------------------------------------------------------------------------------
//*Exemplo básico de uma arrow function que soma dois números
let somar = (a, b) => {
  return a + b;
};
// Chamando a função e exibindo o resultado no console
console.log(somar(2, 8));
//----------------------------------------------------------------------------------
//*Exemplo de arrow function com um único parâmetro (não precisa de parênteses)
let dobrar = (n) => n * 2; // O prettier "corrige" e coloca o parênteses, mas realmente não precisa e funciona.
// Chamando a função e exibindo o resultado no console
console.log(dobrar(7));
//----------------------------------------------------------------------------------
//*Exemplo de uma arrow function usada como callback
let numeros = [1, 2, 3, 4, 5, 6];
// Usando arrow function com o método map para dobrar os valores do array
let numerosDobrados = numeros.map((n) => n * 2);
// Exibindo o array resultante no console
console.log(numerosDobrados);
//----------------------------------------------------------------------------------
//*Arrow function com corpo de função mais complexo
let saudacao = (nome, idade) => {
  let mensagem = `\nOlá, meu nome é ${nome} e tenho ${idade} anos!`;
  return mensagem;
};
// Chamando a função e exibindo o resultado no console
console.log(saudacao("Gabriel", "25"));
