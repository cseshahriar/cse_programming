package calculator;

public class Arithmatic {
	
	// instance variable
	public int add_result;
	
	public int add(int a, int b) {
		return add_result =  a + b; // why this
	}
	
	public void add_result() {
		System.out.println(add_result);
	}
}


