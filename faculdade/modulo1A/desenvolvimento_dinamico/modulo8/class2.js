class carro {
  constructor(modelo, cor, ano) {
    this.modelo = modelo;
    this.cor = cor;
    this.ano = ano;
  }
  declarar() {
    let descricaoCarro = `O carro é do modelo ${this.modelo}, cor ${this.cor} e ano ${this.ano}`;
    return descricaoCarro;
  }
}

const car = new carro("fiat uno", "prata", 2000);
console.log(car.declarar());
