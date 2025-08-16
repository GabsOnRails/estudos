// Declaração de uma variável chamada resultado e atribuição de uma função anônima a ela
let somarParametros = function (parametro1, parametro2) {
  console.log("Parametro 1: " + parametro1);
  console.log("Parametro 2: " + parametro2);
  let resultados = parametro1 + parametro2;

  return resultados;
};
let resultados = somarParametros(5, 4);
console.log("Resultado da soma: " + resultados);

//-----------------------------------------------------------------------------------------------------------
//passando função anônima como argumento para outra função
function executarFuncao(funcao, valor1, valor2) {
  console.log("\nFunção como argumento");
  return funcao(valor1, valor2);
}

let ResultadoFuncao = executarFuncao(somarParametros, 10, 15);
console.log(
  "Resultado com função anterior (somarParametros) como argumento: " +
    ResultadoFuncao
);
//-----------------------------------------------------------------------------------------------------------

//definindo e chamando uma função anônima imediatamente
let resultadoImediato = (function (a, b) {
  console.log("\nFuncão imediata");
  return a * b;
})(4, 5);
console.log("Resultado imediato: " + resultadoImediato);
//-----------------------------------------------------------------------------------------------------------
//! TESTE FEITOS POR MIM SEM ACOMPANHAR, APENAS LEMBRANDO
let funcaoAnonima = function (a, b) {
  console.log("teste 1" + a);
  console.log("teste 2" + b);
  let resultadoTeste = a / b;
  return resultadoTeste;
};

let resultadoTeste = funcaoAnonima(10, 5);
console.log("Resultado da divisão: " + resultadoTeste);
//-----------------------------------------------------------------------------------------------------------
function funcaoDupla(funcaox, x, y) {
  return funcaox(x, y);
}
let resultadofuncaox = funcaoDupla(funcaoAnonima, 20, 4);
console.log("Resultado da função dupla: " + resultadofuncaox);
//-----------------------------------------------------------------------------------------------------------
let funcaoimediata = (function (h, j) {
  return h * j;
})(8, 7);
console.log("Retorno da função imediata: " + funcaoimediata);
