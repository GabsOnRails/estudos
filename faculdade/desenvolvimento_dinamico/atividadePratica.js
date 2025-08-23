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

// 2. Passando parâmetros para funções:

// a. Crie uma função de saudação para aceitar um parâmetro nome.

// b. Dentro da nova função, imprima uma mensagem de saudação personalizada que inclua o nome passado como argumento.

// c. Chame a função novaSaudacao() com diferentes nomes como argumento para testar.

// 3. Crie uma função chamada soma.

// a. Esta função deve aceitar dois parâmetros, a e b, e retornar a soma deles.

// b. Chame a função soma com alguns pares de números como argumentos e imprima o resultado no console.

//função saudacao
function saudacao() {
  console.log("Olá,mundo!");
}

saudacao();

//função novaSaudacao utilizando parâmetros.
function novaSaudacao(nome) {
  console.log(`Olá,${nome}`);
}
novaSaudacao("Gabriel");
novaSaudacao("Ana");
novaSaudacao("Roberto");

//função soma com parâmetros a e b
function soma(a, b) {
  return a + b;
}
console.log(soma(5, 4));
console.log(soma(88, 456));
console.log(soma(18, 8));
