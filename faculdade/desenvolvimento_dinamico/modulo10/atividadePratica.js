//Criando a promessa
let mypromise = new Promise((resolve, reject) => {
  let sucesso = false;
  if (sucesso) {
    resolve("Sucesso!");
  } else {
    reject("Erro!");
  }
});

//implementando a promessa
mypromise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    console.log("Operação Concluída!");
  });
