package final_exam_cse207;
// 1.Can we overload a static method in Java?

/*
 * Can we overload static methods? 
The answer is ‘Yes’. We can have two or more static methods with the same name, 
but differences in input parameters. For example, consider the following 
Java program. 
* */

public class OverrideStaticMethod {
	
	public static void foo() {
        System.out.println("Test.foo() called ");
    }
    public static void foo(int a) {
        System.out.println("Test.foo(int) called ");
    }
    
	public static void main(String[] args) {
		OverrideStaticMethod.foo();
		OverrideStaticMethod.foo(10);

	}

}
// ref: https://www.geeksforgeeks.org/can-we-overload-or-override-static-methods-in-java/#:~:text=Can%20we%20overload%20static%20methods,but%20differences%20in%20input%20parameters.
