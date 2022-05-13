package final_exam_cse207;
// qestion 5 

public class Temperature {

	public static void main(String[] args) {
		double fahrenheit = 62.5; 
		double celsius = f2c(fahrenheit);
		System.out.println(fahrenheit + " F = " + celsius + 'C');

	}
	
 	public static double f2c(double fahrenheit) { 
		return (fahrenheit - 32) * 5 / 9; 
	} 

}
