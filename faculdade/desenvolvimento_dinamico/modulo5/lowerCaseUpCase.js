// converter apenas caracters alfabéticos para lower ou uppercase

//colocando em lowercase
let nome = "Gabriel Felipe";
let lowerCase = nome.toLocaleLowerCase();
console.log(lowerCase);

//colocando em uppercase
let nome2 = "gabriel felipe";
let upperCase = nome2.toUpperCase();
console.log(upperCase);

//colocando números no meio
let numAndWords = "Gabriel Felipe 123!!^^";
let upper = numAndWords.toUpperCase();
console.log(`A string só irá mudar os caracteres alfabéticos: ${upper}`);
