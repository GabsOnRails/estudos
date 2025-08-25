// Exemplos de operadores lógicos
//! Matemática discreta estuda operações lógicas voltadas para computação

const a = true;
const b = false;
const c = true;

//Utilizando o operador && (e)
const resultadoE1 = a && b; //false
const resultadoE2 = a && c; //true
console.log(`Resultado de && entre ${a} e ${b} igual a ${resultadoE1}`);
console.log(`Resultado de && entre ${a} e ${c} igual a ${resultadoE2}`);
console.log("-------------------------------------------------");
//------------------------------------------------------------------------------

//Utilizando operador || (ou)
const resultadoAnd1 = a || b; //true
const resultadoAnd2 = b || false; //false
console.log(`Resultado de || entre ${a} e ${b} igual a ${resultadoAnd1}`);
console.log(`Resultado de || entre ${b} e false igual a ${resultadoAnd2}`);
console.log("-------------------------------------------------");
//------------------------------------------------------------------------------

//Utilizando o operador ! (não)
const resultadoNot1 = !a; //false
const resultadoNot2 = !b; //true
console.log(`Resultado de !a ${a} igual a ${resultadoNot1}`);
console.log(`Resultado de !b ${b} igual a ${resultadoNot2}`);
console.log("-------------------------------------------------");
//------------------------------------------------------------------------------

//Utilizando combinações
const comb1 = (a || b) && !c; //false
const comb2 = a && c && !b; //true
console.log(comb1);
console.log(comb2);
