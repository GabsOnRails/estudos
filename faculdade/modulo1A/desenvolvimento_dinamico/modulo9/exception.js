//Usando try, catch e finally para tratar exceções
//try é o bloco que irá envolver o trecho onde se esperar que o erro ocorra
//o catch serve para pegar essa informação e retornar uma mensagem
//finally é opcional e garante que determinada ação irá acontencer sempre.

//exemplo retirado do site DIO

// function processForm(formData) {
//   try {
//     //processar os dados do formulário
//     const result = formData.username.toUppercase();
//     console.log("Resultado: ", result);
//   } catch (error) {
//     console.error("Erro ao processar formulário:", error.message);
//   } finally {
//     //Limpar os campos do formulário, independentemente de erros
//     clearFormFields(formData);
//   }
// }

// const formData = { username: "usuário" };
// processForm(formData);
//-------------------------------------------------------------------------------

//Outro exemplo
class Imovel {
  constructor(endereco, tamanho) {
    this.endereco = endereco;
    this.tamanho = tamanho;
  }
  descrever() {
    throw new Error("Este método deve ser implementado por subclasses");
  }
  //Método para validação de dados (encapsulamento de exceções)
  validar() {
    if (!this.endereco || !this.tamanho) {
      throw new Error("Dados inválidos para o imovél");
    }
  }
}

//Classe derivada Casa que herda de imóvel
class Casa extends Imovel {
  constructor(endereco, tamanho, numero, garagem) {
    super(endereco, tamanho);
    this.numero = numero;
    this.garagem = garagem;
  }
  descrever() {
    try {
      this.validar();
      let descricao = `Casa localizada em ${this.endereco}, no numero ${this.numero}, com ${this.tamanho}m²`;
      descricao += this.garagem ? " e tem garagem." : " e não possui garagem.";
      return descricao;
    } catch (error) {
      throw new Error(`Erro ao descrever a casa: ${error.message}`);
    }
  }
}

//Polimorfismo
function descreverImovel(imovel) {
  try {
    console.log(imovel.descrever());
  } catch (error) {
    console.error(error.message);
  } finally {
    //Essa ação sempre irá ocorrer
    console.log("olá mundo");
  }
}

//Criação de objetos (instanciando classes)
const minhaCasa = new Casa("rua principal", "525", 55);
descreverImovel(minhaCasa);
