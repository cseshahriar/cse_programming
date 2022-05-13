package final_exam_cse207;
import java.util.Scanner;

// 4.Write a program to print the sum of two numbers entered by user bydefining your own method

public class Summation {
	static Scanner in = new Scanner(System.in);

	public static void main(String[] args) {
		double num1 = get_input();
		double num2 = get_input();
		
		get_summation(num1, num2);
	}
	
	public static double get_input() {
		System.out.print("Input the 1st number: ");
		return in.nextDouble();
	}
	
	public static void get_summation(double a, double b) {
		System.out.println( a + b); 
	}
	
} 