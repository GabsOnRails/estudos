// Faça enquanto. Primeiro executa o bloco de código, depois entra no loop.
// Usamos quando precisamos que o bloco seja executado pelo menos uma vez.

// Imagine que quer aprender a andar de bibliceta e precisa ficar pelo menos 3 minutos sem cair.

time = 0;
fall = false;

do {
  if (time <= 0) {
    minute = "minuto";
  } else {
    minute = "minutos";
  }
  time++;
  console.log(`Andei por ${time} ${minute}, sem cair!`);
  if (time === 3) {
    fall = true;
  }
} while (!fall && time < 3);
