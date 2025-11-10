package files;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;


public class FileWriteExample {
    public static void main (String [] args) {
        //Escrita
        try (
                BufferedWriter writer = new BufferedWriter(new FileWriter("arquivo.txt"))
                ) {
            writer.write("Olá, Mundo!");
            writer.newLine();
            writer.write("Segunda linha");
            System.out.println("Arquivo criado.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
