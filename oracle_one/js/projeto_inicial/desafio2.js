// Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".
// Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.
// Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre "Tente novamente para ganhar.".
// Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.
// Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.

let nome = promp('Qual seu nome?');
alert ('Seja bem vindo'+nome);

let semana = prompt('Qual dia da semana é hoje?')
if (semana == 'sabado','domingo') {
    alert('Bom final de semana')+nome}
else {
        alert('Boa semana'+nome);
    }

let numero = promt('Digite um número:')
if (numero >= 0) {
    alert('Número positivo!')
}
else{'Número negativo.'}

saldoDisponivel = 0
saldoConta = 2000
alert('Seu saldo é'+saldoConta);
