import java.util.Scanner;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (true) {
			String text = input.nextLine();

			if (text.length() == 1) {
				break;
			}
			ArrayList<Character> stack = new ArrayList<Character>();
			boolean judge = true;
			for (int i = 0; i < text.length(); i++) {
				char check = text.charAt(i);
				if ( check == '(' | check == '[') {
					stack.add(check);
				} else if (check == ')') {
					if (stack.size() != 0 && stack.get(stack.size() - 1) == '(') {
					stack.remove(stack.size() - 1);
				    } else {
				    	judge = false;
				    	break;
				    }
				} else if (check == ']') {
					if (stack.size() != 0 && stack.get(stack.size() - 1) == '[') {
						stack.remove(stack.size() - 1);
					} else {
						judge = false;
						break;
					}
				}
			}	
			if (stack.size() == 0 && judge == true) {
				System.out.println("yes");
			} else {
				System.out.println("no");
			}			
		}		
	}
}