package first_class;

public class Main {

	public static void main(String[] args) { // strings args = one more argument received
		// no need object if static
		// publicly accicble
		// void means no return
		
		int first = 10;
		int second = 20;
		
		System.out.println(first + " " + second);
		
		// add two number
		int sum = first + second;
		System.out.println("The sum is : "+ sum);
		
		// create object for another class
		
		Shahriar obj = new Shahriar();
		obj.shahriar_print();
	}

}


class Shahriar {
	int  a = 10;
	
	// constructor
	public void shahriar_print() {
		System.out.println("Shahriar");
	}
}