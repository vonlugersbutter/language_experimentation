import java.util.Scanner;

public class UsingInputs {
  public static void main(String[] args) {
    String name;
    int age;
    Scanner in;

    in = new Scanner(System.in);
    System.out.print("What is your name, hero? ");
    name = in.next();
    System.out.println("Ah. So your name is " + name + ".");

    System.out.print("And how old are you? ");
    age = in.nextInt();

    int age_of_sage = age + 4;

    System.out.println("I am 4 years older than you. I am " + age_of_sage + " years old.");

    System.exit(0);
    in.close();
  }
}
