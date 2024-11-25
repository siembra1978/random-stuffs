import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

      Scanner input = new Scanner(System.in);
      Random random = new Random();

      int guessTotal = 1;

      System.out.println("I'm thinking of a random number. Guess it.");

      int number = random.nextInt(101);
      //System.out.println(number);
      
      while (guessTotal <= 10){

        System.out.println("Guess " + guessTotal + ":");

        if (!input.hasNextInt()){
          System.out.println("Not a valid integer.");
          input.next();
          continue;
        }

        int guess = input.nextInt();

        if (guess == number){
          System.out.println("hip hip hurray!");
          break;
        }
        else if (guess > number){
          System.out.println("Your guess is greater than my number");
        }
        else if (guess < number){
          System.out.println("Your guess is less than my number");
        }

        guessTotal++;
      }

      if (guessTotal > 10){
        System.out.println("Sorry, you failed.");
      }

      input.close();
    }
  }