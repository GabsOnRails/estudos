// Sabemos que existem algumas maneiras de armazenar uma coleção de objetos, uma delas com arrays, que armazenam um conjunto de itens que tenham o mesmo tipo de dado primitivo ou o mesmo objeto. Os itens são armazenados em forma de tabelas de fácil manipulação, sendo diferenciados e referenciados por um índice numérico. (Furgeri, 2002). Diante disso, o que o código a seguir produz?
public class QuestaoAula6 {


         public static void main(String[] args) {

                 

                  String [] objetos = {"garrafa","copo","litro"};

                  for (int tam = objetos.length - 1; tam >= 0; tam--){

                           System.out.print(objetos[tam] + " ");

                  }

         }

}