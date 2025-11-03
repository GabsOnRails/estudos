public class pratica {
    public static void main (String [] args) {
        int[] numbers = {1, 2, 3, 4, 5}; // Array com inicialização auto
        String[] names = {"Alice", "Bob", "Charlie"};

        int[] numeros = new int[5];
        numeros[0] = 2;
        numeros[1] = 35;
        numeros[2] = 80;
        numeros[3] = 45;
        numeros[4] = 100;

        System.out.println("Vetor de números inic valores: " + numbers);
        System.out.println("Vetor de nomes inic valores: " + names);
        //Aqui o resultado sai estranho, pois não podemos acessar diretamente os valores.

        //Precisamos percorrer com um for:
        System.out.println("Valores usando o for:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Valores com o for no indice [" + i + "]" + numbers[i]);
        }

        System.out.println("Valores usando o for:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Valores com o for no indice [" + i + "]" + numeros[i]);
        }
    }
}


