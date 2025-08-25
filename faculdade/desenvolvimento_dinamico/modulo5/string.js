//slice -> Fatiar, faz o recorte em determinado período

let frutas = "maçã,banana,laranja,uva,abacaxi";
console.log(`Tamanho da string frutas: ${frutas.length}`);

//usando o slice para pegar uma parte específica da string
let sliceFrutas = frutas.slice(5, 21);
console.log(`resultado da string fatiada: ${sliceFrutas}`);
let sliceFrutas2 = frutas.slice(24, 31);
console.log(`resultado da string fatiada: ${sliceFrutas2}`);

//trim -> Cortar, tira os espaços vazios no ínicio e fim da string
let fruitWithSpace = "      pera     ";
let space = fruitWithSpace.trim();
console.log(`resultado da string sem espaço: ${space}`);

//Precisamos declarar outra lista para frutas

//split -> Separar, serve para separar a string de acordo com um critério
let listOfFruits = "maçã,pera,uva,abacate,morango";
let arrayFruits = listOfFruits.split(",");
console.log("resultado do array", arrayFruits);
