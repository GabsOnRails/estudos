package instrucoes;

public class condicional {
public static void main (String [] args) {

    int numero = 10;

    if (numero > 0) {
        System.out.println("O número é positivo.");
    }
    else if (numero < 0) {
        System.out.println("O número é negativo.");
    }

    if (numero%2 == 0) {
        System.out.println("O número é par.");
    } else {
        System.out.println("O número é impar.");
    }

}
}