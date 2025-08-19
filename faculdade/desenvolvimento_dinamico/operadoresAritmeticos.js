//Operações aritméticas

//Operações aritméticas básicas

//Calculadora
function calculadora(num1, num2) {
  //Soma
  let adicao = num1 + num2;
  //Subtração
  let subtracao = num1 - num2;
  //Divisão
  let divisao = num1 / num2;
  //Multiplicação
  let multiplicacao = num1 * num2;
  //Módulo
  let modulo = num1 % num2;
  //Exponêncial
  let exponencial = num1 ** num2;

  //Declarando a let para incremento e decremento, caso contrário irá mudar os resultados
  //Incremento num1
  let incrementar = num1; //Aqui a variável pega o parâmetro passado na função e armazena, sem mudar o resultado para as demais operações
  incrementar++;
  //Decremento num2
  let decrementar = num2;
  decrementar--;

  //Exibindo resultado
  console.log(`Adição de ${num1} + ${num2} é igual a: ${adicao}`);
  console.log(`Subtração de ${num1} - ${num2} é igual a: ${subtracao}`);
  console.log(`Divisão de ${num1} / ${num2} é igual a: ${divisao}`);
  console.log(`Multiplicação de ${num1} * ${num2} é igual a: ${multiplicacao}`);
  console.log(`O módulo de ${num1} % ${num2} é igual a: ${modulo}`);
  console.log(`O exponêncial de ${num1} ** ${num2} é igual a: ${exponencial}`);
  console.log(`O incremento de ${num1} é igual a: ${incrementar}`);
  console.log(`O decremento de ${num2} é igual a: ${decrementar}`);
}

//Chamando função e declarando os parâmetros
calculadora(10, 5);
