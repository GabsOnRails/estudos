//Como criar uma classe, um objeto e declara.

//classe

class animal {
  constructor(raca, cor, nome, idade) {
    this.cor = cor;
    this.nome = nome;
    this.idade = idade;
    this.raca = raca;
  }
  declarar() {
    let descricao = `O animal da raça ${this.raca} e cor ${this.cor}, se chama ${this.nome} e tem ${this.idade} anos.`;
    return descricao;
  }
}

const pet = new animal("vira-lata", "caramelo", "chiquinho", 4);
console.log(pet.declarar());
