// Don't touch it right now I need to fix it

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class MorePractice {
  public static void main(String[] args) {
    String name;
    Scanner in;

    in = new Scanner(System.in);
    System.out.print("What is your name, hero? ");
    name = in.next();
    System.out.println("Ah. So your name is " + name + ".");

    System.out.println("Let's see if you know how to add properly.");
    int a_number = ThreadLocalRandom.current().nextInt(0, 100 + 1);
    int another_number = ThreadLocalRandom.current().nextInt(0, 100 + 1);
    int sum = a_number + another_number;

    System.out.print("What do you think the sum of " + a_number + " and " + another_number + " is? ");
    int user_guess = in.nextInt();

    if (user_guess == sum) {
      System.out.println("Yep, that's correct! The sum is " + sum + ".");
    }
    else {
      System.out.println("Nope, the sum is actually " + sum + ".");
    }

    System.exit(0);
    in.close();
  }
}
