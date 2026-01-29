public class atividadePratica {
    public static void main (String [] args) {
        //Declaração de variáveis
        int diferenca = 26;
        int numero = 15;
        float preco =  25;
        boolean desativado = false;
        try {
            if (numero > preco) {
                int troco = numero - diferenca;
                System.out.println("O troco é de: " + troco + " reais ");
            } else {
                throw new IllegalArgumentException("O valor deve ser maior que o preço");
            }
            // Erro
        } catch (IllegalArgumentException e) {
            System.out.print("Erro capturado: " + e.getMessage());
        }
        //Uso do booleano
        if (desativado == false) {
            System.out.println("\nCaixa eletrônico desativo, não é possível fazer saque.");
        }
        //Uso da matriz e vetores
        int [] posicaoFila = {1,2,3,4,5,6};
        for(int n:posicaoFila) {
            System.out.println("Numero de posição na fila: " + n + "/6");
        }
        int [][] matrizOpcoes = {{1,2,3},
                                 {4,5,6},
                                 {7,8,9},
                                 {10,11,12}};
        System.out.println("Opções válidas: ");
        for (int i = 0; i < matrizOpcoes.length; i ++) {
            for (int j = 0; j < matrizOpcoes[i].length; j++) {
                System.out.print(matrizOpcoes[i][j] + " ");
            }
            System.out.println();
        }
    }
}
