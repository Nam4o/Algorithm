import java.util.Scanner;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		ArrayList<Integer> list1 = new ArrayList<Integer>();
		ArrayList<Integer> list2 = new ArrayList<Integer>();
		
		int i = 9;
		
		boolean check = false;
		
		for (i = 0; i < 9; i++) {
			int score1 = input.nextInt();
			list1.add(score1);
		}
		
		for (i = 0; i < 9; i++) {
			int score2 = input.nextInt();
			list2.add(score2);
		}
		
		int team1 = 0;
		int team2 = 0;
		
		for (i = 0; i < 9; i++) {
			team1 += list1.get(i);
			if (team1 > team2) {
				check = true;
			}
			team2 += list2.get(i);
			
		}
		
		if (check) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
		
	}

}
