import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int T = input.nextInt();
		
		for (int tc = 1; tc <=T; tc ++) {
			
			int s = input.nextInt();
			int N = input.nextInt();
			for (int buy = 0; buy <N; buy ++) {
				int p = input.nextInt();
				int q = input.nextInt();
				s += p * q;
			}
			System.out.println(s);						
		}
	}
}
