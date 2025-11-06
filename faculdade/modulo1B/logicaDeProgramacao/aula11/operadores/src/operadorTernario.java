public class operadorTernario {
    public static void main (String[]args){
        //resultado = condicao ? verdadeiro : falso;

        //Declarando variaveis
        int a = 51;
        int b = 25;

        //Usando operador ternario
        String validacao = (a > 20) ? "A é maior que 20" : "A é menor que vinte";
        System.out.println(validacao);

        //Maior número
        int maior = (a > b) ? a : b ;
        System.out.println("O maior valor entre " + a + " e " +b+ " é: " +maior);

        //Usando operadores lógicos

        String logicos = (a > b && a > 50) ? "A é o maior número e maior que cinquenta." :
                "A não atende os requisitos de ser maior que B e que 50.";
        System.out.println(logicos);
    }
}
