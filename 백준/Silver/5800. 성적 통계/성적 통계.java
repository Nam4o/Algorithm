import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int tc = input.nextInt();
		
		for (int i = 1; i <= tc; i++) {
			System.out.println("Class " + i);
			int len = input.nextInt();
			ArrayList<Integer> score = new ArrayList<Integer>();
			for (int j = 0; j < len; j++) {
				score.add(input.nextInt());
			}
			score.sort(Comparator.reverseOrder());
			int mx_gap = 0;
			for (int t = 0; t < score.size() - 1; t++) {
				if (score.get(t) - score.get(t + 1) > mx_gap) {
					mx_gap = score.get(t) - score.get(t + 1);
				}
			}
			System.out.println("Max " + score.get(0) + ", Min " +
			score.get(score.size() - 1) + ", Largest gap " + mx_gap);
		}
	}
}
