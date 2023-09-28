import java.util.Scanner;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		ArrayList<Integer> list = new ArrayList<Integer>();
		int answer;
		
		int i;
		for (i = 0; i < N; i ++ ) {
			answer = input.nextInt();
			list.add(answer);
		}

		int cnt = 0;
		int amount = 0;
		
		int j;
		for ( j = 0; j < N; j ++) {
			if (list.get(j) == 1) {
				cnt += 1;
				amount += cnt;
			} else {
				cnt = 0;
			}
		}
		System.out.println(amount);
	}
}
