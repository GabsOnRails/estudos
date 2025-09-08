//Aqui irei usar o poliformismo e abstração

//Criação de classe base
class Carro {
  constructor(modelo, ano) {
    this.modelo = modelo;
    this.ano = ano;
  }
  //Metódo de abstração para descrever o carro (deve ser implementado nas sub-classes)
  descrever() {
    throw new Error("Este metódo deve ser adicionado a sub-classes");
  }
}

//Criação de classe derivada Fiat, irá herdar de Carro
class Fiat extends Carro {
  constructor(modelo, ano, cor, abs) {
    super(modelo, ano);
    this.cor = cor;
    this.abs = abs;
  }
  descrever() {
    let descricao = `O carro do modelo ${this.modelo}, do ano ${this.ano} e da cor ${this.cor}`;
    descricao += this.abs ? " possui abs." : " não possui abs.";
    return descricao;
  }
}

//Função para descrever o Carro (polimorfismo)
function ModeloCarro(Carro) {
  console.log(Carro.descrever());
}

class Porsche extends Carro {
  constructor(modelo, ano, cor, abs) {
    super(modelo, ano);
    this.cor = cor;
    this.abs = abs;
  }
  descrever() {
    let descricao = `O carro do modelo ${this.modelo}, do ano ${this.ano} e da cor ${this.cor}`;
    descricao += this.abs ? " possui abs." : " não possui abs.";
    return descricao;
  }
}

const carro1 = new Fiat("Fiat Uno", 2000, "Amarelo", false);
const carro2 = new Porsche("Porsche", 2015, "Prata", true);

ModeloCarro(carro1);
ModeloCarro(carro2);
