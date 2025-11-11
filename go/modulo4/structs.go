//go:build ignore

package main

import (
	"fmt"
)

func main () {
//forma de declarar uma struct:
type Pessoa struct { 
Nome string
Idade int
Sobrenome string
}

type Profissao struct {
Pessoa
Profissao string
}

//Como definir os valores dos campos:
fmt.Println(Pessoa{"Gabriel",25,"Felipe"})
fmt.Println(Pessoa{Nome: "Gabriel", Idade: 25, Sobrenome: "Felipe"})

//Atrelando a struct a uma variável para acessar os valores individualmente.
p1 := Pessoa{Nome: "Bento",Idade: 6}
fmt.Println(p1.Nome)

//Alterando o valor de um campo.
p1.Idade = 3
fmt.Println(p1.Idade)

//Declarando um novo tipo, podemos usar ele para fazer varias coisas.
pessoa1 := Pessoa{Nome: "Nicolas", Idade: 38, Sobrenome: "Cage"}
pessoa2 := Pessoa{Nome: "Xuxui", Idade: 999, Sobrenome: "da Silva"}

pessoas := []Pessoa{}
pessoas = append(pessoas,pessoa1,pessoa2) // preciso passar o slice que será adicionado.
fmt.Println(pessoas)

//podemos juntar maps com structs
alunos := map [string] []Pessoa{} // O []Pessoa significa que é uma lista do tipo Pessoa.
alunos["programação"] = pessoas
fmt.Println(alunos)

//Outra forma de juntar maps com structs.
cloud := map [string] []Pessoa{
	"CloudDev": {{Nome: "Jose", Idade: 24, Sobrenome: "Oliveira"}},
	"CloudInfra": {{Nome: "Chico", Idade:89, Sobrenome: "Rio"},{Nome: "Roberto", Idade: 12, Sobrenome: "Zezinho"}},
	//Sempre que for usar esse formato, lembrar de colocar o valor entre {{}}
	// O primeiro par é para definir o valor {}, o segundo para armazenar um 	conjunto do valor.
}
fmt.Println(cloud)

dev := Profissao{pessoa1,"dev"}
fmt.Println(dev)

//Como acessar os campos.

fmt.Println(dev.Profissao) // O que criamos.
fmt.Println(dev.Pessoa.Idade) // O que herdamos da outra struct.
}



