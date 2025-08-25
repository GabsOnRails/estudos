// Usando switch case para avaliar se podemos atravessar ou não.

//declarando função

function lightColor(color) {
  switch (color) {
    case "verde":
      console.log("Pode atravessar.");
      break;
    case "amarelo":
      console.log("Prepare-se para parar.");
      break;
    case "vermelho":
      console.log("Pare! Não atravesse.");
      break;
    default:
      console.log("Cor inválida. Aguarde pela mudança de cor.");
  }
}

//Chamando a função
lightColor("verde");
lightColor("amarelo");
lightColor("vermelho");
lightColor("azul");
