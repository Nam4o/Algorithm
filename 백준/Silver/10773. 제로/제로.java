import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int K = input.nextInt();
		
		ArrayList<Integer> stack = new ArrayList<Integer>();
		
		for (int i = 0; i < K; i++) {
			
			int number = input.nextInt();
			
			if (number != 0) {
				stack.add(number);
			} else {
				stack.remove(stack.size() - 1);
			}
		}
		
		int sum = 0; 
		for (int j = 0; j < stack.size(); j ++) {
			sum += stack.get(j);
		}
		System.out.println(sum);
	}

}
