# 🐹 Estudos em Go (Golang)

Bem-vindo ao meu cantinho de estudos em **Go**, a linguagem criada pelo
Google que promete simplicidade, velocidade e umas dores de cabeça
ocasionais (mas no bom sentido 😅).

Este repositório reúne meus aprendizados, testes, experimentos e códigos
escritos enquanto exploro o ecossistema Go. Se você também está
estudando, fique à vontade para explorar --- talvez encontre algo útil
(ou pelo menos curioso).

------------------------------------------------------------------------

## 📚 O que você vai encontrar aqui

-   📝 Exercícios e projetos iniciais\
-   📘 Conceitos fundamentais da linguagem\
-   🧪 Testes variados\
-   📂 Uma coleção organizada do meu processo de aprendizado

------------------------------------------------------------------------

## 🚀 Objetivo

Aprender Go de forma progressiva --- começando pelo básico (variáveis,
tipos, funções) e avançando até temas como goroutines, canais,
interfaces, concorrência e tudo que, no início, parece confuso mas
depois vira satisfação pura 😄.

------------------------------------------------------------------------

## 💬 Sobre este repositório

Este espaço é dedicado totalmente ao aprendizado, então espere:

-   Comentários sinceros dentro dos códigos\
-   Exemplos que provavelmente revisarei no futuro\
-   A evolução natural de alguém estudando Go do zero até... onde der!

------------------------------------------------------------------------

# 🧪 Como faço os testes
(PS: Nesse repositório, a pasta "exercícios" não contêm testes.)
<br/>
<br/>
Para realizar testes em qualquer exercício, sigo este fluxo:

------------------------------------------------------------------------

### **1. Entrar na pasta do exercício**

``` bash
cd exercícios/returnNegative
```

------------------------------------------------------------------------

### **2. Instalar as dependências de testes (se necessário)**

``` bash
go get github.com/onsi/ginkgo/v2
go get github.com/onsi/gomega
```

------------------------------------------------------------------------

### **3. Se for o primeiro teste da pasta, gerar configuração do Ginkgo**

``` bash
ginkgo bootstrap
```

------------------------------------------------------------------------

### **4. Criar o arquivo de teste usando o padrão**

``` go
package nomedopackage_test

import (
    . "github.com/onsi/ginkgo/v2"
    . "github.com/onsi/gomega"
    "modulo5/nomedopackage"
)

var _ = Describe("MinhaFuncao", func() {
    It("deve retornar o valor correto", func() {
        Expect(nomedopackage.MinhaFuncao(10)).To(Equal(20))
    })
})
```

------------------------------------------------------------------------

### **5. Executar os testes com Go**

``` bash
go test ./...
```

ou:

``` bash
go test
```

------------------------------------------------------------------------

### **6. Opcional: rodar testes com o próprio Ginkgo**

``` bash
ginkgo
```

Modo verboso:

``` bash
ginkgo -v
```

------------------------------------------------------------------------

Com isso, todos os exercícios ficam organizados com testes automatizados
no mesmo padrão do Codewars.

------------------------------------------------------------------------

## 🙌 Bora codar!

Se quiser trocar ideia sobre Go, bugs, dicas ou descobertas, só chamar!

![Gopher
GIF](https://gist.githubusercontent.com/brudnak/efd7b887bd7c0441d8bb88ae1c77374a/raw/4629432d2259da168960c36e3801642960e645cf/gopher-workout.gif)
