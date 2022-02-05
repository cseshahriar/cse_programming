package calculator;
// user input
import java.util.Scanner;


public class Calculator {

	public static void main(String[] args) {
		
		// Scanner obj
		Scanner scanner = new Scanner(System.in);
		System.out.println("Please input for a ");
		int a = scanner.nextInt();
		System.out.println("Please input for  b");
		int b = scanner.nextInt();
		
		Arithmatic arthmatic_obj = new Arithmatic();
		
		// add 
		arthmatic_obj.add(a, b);
		arthmatic_obj.add_result();
		
		
	}

}
