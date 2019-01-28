// Don't touch it right now I need to fix it

import java.util.Scanner;

public class Hangman {
  public static void main(String[] args) {
    String name;
    Scanner in;

    in = new Scanner(System.in);
    System.out.print("What is your name, hero? ");
    name = in.next();
    System.out.println("Ah. So your name is " + name + ".");

    System.out.println("Let's play hangman. I'll think of a word and you have to guess it in 10 tries. You only lose tries if you get a letter wrong.");

    //make this an array
    String secret_word = "morning";
    String[] secret_word_list;
    String[] secret_word_secret_word.split('\s');

    int length_of_word = secret_word.length();
    System.out.println("The word I am thinking of has " + length_of_word + " letters.");

    //make this an array
    String guess_storage = ("");

    while (attempts > 0) {
      int blank_spaces = 0;

      for (String letter : secret_word_list) {
        boolean contains = Arrays.stream(guess_storage_list).anyMatch(letter::equals);

        if (contains == true) {
          System.out.println(letter);
        }

      }
    }


    System.exit(0);
    in.close();
  }
}
