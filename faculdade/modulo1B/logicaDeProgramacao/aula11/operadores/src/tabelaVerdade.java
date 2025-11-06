public class tabelaVerdade {
    public static void main(String[] args){
        // && -> And | || -> Or
        //Declarando variáveis
        boolean x = true;
        boolean y = false;
        boolean a =true;
        boolean b = false;

        //Fazendo comparações
        System.out.println(a&&x); //True
        System.out.println(a&&b); // False
        System.out.println(x&&y); //False

        //Pulando linha
        System.out.println();

        // Usando Or(||)
        System.out.println(a||b); //True
        System.out.println(x||y); // True
        System.out.println(b&&y); //False
    }
}
