package final_exam_cse207;
import java.util.Scanner;

public class GreatestNumber {

	public static void main(String[] args) {
		// scanner obj
		Scanner in = new Scanner(System.in);
		
		System.out.print("Input the 1st number: ");
		int num1 = in.nextInt();
		   
		System.out.print("Input the 2nd number: ");
		int num2 = in.nextInt();
		   
		System.out.print("Input the 3rd number: ");
		int num3 = in.nextInt();
		   
		   
		if (num1 > num2)
			if (num1 > num3)
				System.out.println("The greatest: " + num1);
		   
		if (num2 > num1)
			if (num2 > num3)
				System.out.println("The greatest: " + num2);
		   
		if (num3 > num1)
			if (num3 > num2)
				System.out.println("The greatest: " + num3);
		
	}

}

// ref : https://www.w3resource.com/java-exercises/conditional-statement/java-conditional-statement-exercise-3.php
