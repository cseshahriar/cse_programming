package final_exam_cse207;
import java.util.Scanner;

/*
 * Author: Md. Shahriar Hosen
 * ID: 2116CSE50201
 * */
public class GreatestNumber {
	static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {
		
		int num1 = get_input();
		int num2 = get_input();
		int num3 = get_input();
		   
		   
		if (num1 > num2 && num1 > num3)
				System.out.println("The greatest: " + num1);
		   
		if (num2 > num1 && num2 > num3)
				System.out.println("The greatest: " + num2);
		   
		if (num3 > num1 && num3 > num2)
				System.out.println("The greatest: " + num3);
		
	}
	
	public static int get_input() {
		System.out.println("Please enter a int number ");
		return scanner.nextInt();
		
	}

}
