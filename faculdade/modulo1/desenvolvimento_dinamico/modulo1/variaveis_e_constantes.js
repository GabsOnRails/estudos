//var ninguém usa isso mais
// Declaração de uma variável usando o var
function exemploVar() {
    if (true) {
        var mensagem = "Olá, faculdade Descomplica! Eu sou uma var...";
    }
    console.log(mensagem); 
}
exemploVar(); 

//mensagem externa
var mensagem = "Olá, faculdade Descomplica! Eu sou uma var externa...";
console.log(mensagem);



//let escopo é de bloco -> usam mais pois consegue ver onde está sendo usada
function exemplolet() {
    if (true) {
        let mensagem = "Olá, faculdade Descomplica! Eu sou uma let...";
        console.log(mensagem); // Acessível dentro do bloco
    }
    //console.log(mensagem); // Isso causaria um erro, pois mensagem não está definida aqui
}
exemplolet();

//var e let não podem ser redeclaradas no mesmo escopo
//let mensagem = "Olá, faculdade Descomplica! Eu sou uma let externa...";
//console.log(mensagem);


//const não pode ser alterada, nem redeclarada
const externo = "Olá, faculdade Descomplica! Eu sou uma const externa...";

//usando const dentro de uma função
function exemploConst() {
    const mensagem = "Olá, faculdade Descomplica! Eu sou uma const...";
    console.log(mensagem); // Acessível dentro do bloco
}
exemploConst();

console.log(externo); // Acessível fora do bloco

/*
comentários em bloco
teste linha 2
*/

/**
 * Dessa forma o javascript consegue gerar documentação automática do código.
 * Comentários em bloco são usados para documentar o código,
 * explicar a lógica por trás de uma função ou variável,
 * @param {string} nome - O nome da pessoa a ser saudada.
 * @returns {string} A saudação personalizada.
 * @example
 * Exemplo de uso:
 * console.log(saudacao("João")); // Saída: Olá, João!
 */

function saudacao(nome) {
    return `Olá, ${nome}!`;
}   
let resultado = saudacao("João");
console.log(resultado); // Saída: Olá, João!

