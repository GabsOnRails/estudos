// Loop que ocorre enquanto (while) uma condição específica é verdadeira.
// Precisa ter a condição inicial e o que irá fazer parar

// Imagine que estou contabilizando minhas flexões e quero ir até o cansaço.

pushUp = 0;
cansaco = false;

while (!cansaco) {
  pushUp++;
  console.log(`Eu fiz ${pushUp} flexões até o momento.`);
  if (pushUp === 20) {
    cansaco = true;
  }
}
