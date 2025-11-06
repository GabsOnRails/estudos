//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class operadores {
    public static void main(String[] args) {
        int x = 10;
        int y = 4;

        //Operadores aritméticos (+, - , x , /, %, **)
        int soma = x + 4;
        System.out.println(soma);

        int subtracao = y - 2;
        System.out.println(subtracao);

        int multiplicacao = y * 2;
        System.out.println(multiplicacao);

        int divisao = x / 2;
        System.out.println(divisao);

        int modulo = x % 3;
        System.out.println(modulo);

        // O exponencial precisa da lib math

        //Operadores de atribuição

        int z = 4;
        int h = 2;
        //Print mostrando valores
        System.out.println("Valores antes das operações: z: " +z + " h:"+h);
        // Incremento
        z += 1;
        System.out.println("Valor após atribuição z: "+z);

        // Decremento
        h -= 1;
        System.out.println("Valor após decremento h: "+h);
        // Multiplicamento
        z *= 2;
        System.out.println("Valor após multiplicamento z: "+z);
    }
}