package calculator;

public class Arithmatic {
	
	// instance variable
	public int add_result;
	
	
	/*
	 * A constructor in Java is a special method that is used to initialize objects. The constructor is called when an object of a class is created. It can be used to set initial values for object attributes:
	 */
	public Arithmatic() { // no need to clll, class name
		System.out.println("Arithmatic constructor call");
	}
	
	// method
	public int add(int a, int b) {
		return add_result =  a + b; // why this
	}
	
	// method
	public void add_result() {
		System.out.println(add_result);
	}
}


