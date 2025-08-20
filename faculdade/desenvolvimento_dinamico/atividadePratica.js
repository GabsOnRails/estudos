// Instruções

// Título da Prática: Criação de funções em JavaScript

// Objetivos: Criar e entender como funcionam funções em JavaScript

// Primeiramente, leia atentamente o texto.

// Criar uma função em JavaScript é definir um bloco de código que pode ser executado repetidamente em resposta a um evento, a uma chamada de outra parte do código ou por meio de um temporizador.

// Em JavaScript, uma função é definida usando a palavra-chave function, seguida pelo nome da função e, opcionalmente, uma lista de parâmetros entre parênteses. O corpo da função é delimitado por chaves {} e contém o código que será executado quando a função for chamada.

// Agora, vamos praticar!

// 1. Criando funções simples:

// a. acesse o LabTech.

// b. Crie um codigo JavaScript chamado funcoes.js.

// c. Neste código, crie uma função chamada saudacao, que simplesmente imprime “Olá, mundo!” no console.

// d. A função deverá chamar saudacao().

//funcão saudacao
function saudacao() {
  console.log("Olá, mundo!");
}

// 2. Passando parâmetros para funções:
function novaSaudacao(nome) {
  console.log(`Olá, ${nome}!`);
}

// 3. Crie uma função chamada soma.
function soma(a, b) {
  return a + b;
}

//imprimindo resultados
//funcao saudacao
saudacao();
//funcao novaSaudacao
novaSaudacao("Gabriel");
novaSaudacao("Ana");
novaSaudacao("Hilio");
//funcao soma
console.log(`Resultado da soma: ${soma(4, 5)}`);
console.log(`Resultado da soma: ${soma(1990, 35)}`);
console.log(`Resultado da soma: ${soma(2, 13456)}`);
