import java.io.*;
import java.util.*;

public class Main {
	
	static int n, m;
	static int[][] square;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}
		square = new int[n][m];
		
		int mx = 0;
		
		for (int i = 0; i < n; i++) {
			String line = br.readLine();
			for (int j = 0; j < m; j++) {
				square[i][j] = Integer.parseInt(String.valueOf(line.charAt(j)));
				if (mx == 0 && square[i][j] != 0) {
					mx = 1;
				}
				if (i != 0 && j != 0 && square[i][j] != 0) {
					if (square[i][j - 1] != 0 && square[i - 1][j] != 0 && square[i - 1][j - 1] != 0) {
						square[i][j] = Math.min(Math.min(square[i][j - 1], square[i - 1][j]), square[i - 1][j - 1]) + 1;
						if (square[i][j] > mx) {
							mx = square[i][j];
						}
					}
				}
			}
		}
		System.out.println(mx*mx);
		
	}
}
