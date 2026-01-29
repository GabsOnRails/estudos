public class operadoresLogicos {
    public static void main (String[]args){
        //Operadores logicos são and (&&), or(||) e not (!)

        //declarando variaveis
        boolean a = true;
        boolean b = false;

        //Exibindo variaveis
        System.out.println("Variável A: "+a+"\nVariável B: "+b);

        //Usando operadores logicos
        //And
        System.out.println("a&&b: " + (a&&b)); // False porque B é falso.

        //Or
        System.out.println("a||b: " + (a||b)); // True porque A é verdadeiro.

        //Not
        System.out.println("!a: " + (!a)); // False porque A é verdadeiro.
        System.out.println("!b:" + (!b)); // True porque B é falso.
    }
}
