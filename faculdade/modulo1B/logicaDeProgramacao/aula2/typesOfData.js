//types of data

// //string
// console.log("Esse é um dado alphanúmerico: Debora");

// //int
// console.log("Esse é um dado inteiro: " + 10);

// //float
// console.log("Esse é um dado float(real): " + 2.3);

// //logic
// console.log("Esse é um dado lógico(booleano): " + false);

//---------------------------------------------------------------//

//Atividade prática
let nome = "Ruby";
let idade = 10;
let altura = 1.55;
if (idade <= 10) {
  crianca = "é criança";
} else {
  crianca = "não é mais criança";
}

function identificacao(nome, idade, altura, crianca) {
  frase = `${nome}, tem ${altura} cm, ${idade} anos e ${crianca}`;
  console.log(frase);
}

identificacao(nome, idade, altura, crianca);
