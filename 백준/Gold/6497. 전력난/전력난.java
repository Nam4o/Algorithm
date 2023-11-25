import java.io.*;
import java.util.*;

public class Main {
	static int n, m, allcost;
	static int[] home;
	static int[][] road;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				n = Integer.parseInt(st.nextToken());
				m = Integer.parseInt(st.nextToken());
			}
			if (n == 0 && m == 0) {
				System.out.println(sb);
				break;
			} else {
				home = new int[n]; road = new int[m][3];
				allcost = 0;
				for (int h = 0; h < n; h++) {
					home[h] = h;
				}
				for (int i = 0; i < m; i++) {
					st = new StringTokenizer(br.readLine());
					while (st.hasMoreTokens()) {					
						road[i][0] = Integer.parseInt(st.nextToken());
						road[i][1] = Integer.parseInt(st.nextToken());
						road[i][2] = Integer.parseInt(st.nextToken());
						allcost += road[i][2];
					}				
				}
				
				Arrays.sort(road, (o1, o2)-> {return o1[2] - o2[2];});
				int cnt = 1;
				int amount = 0;
				for (int h = 0; h < n; h++) {
					home[h] = h;
				}
				for (int j = 0; j < m; j++) {
					if (cnt == n) {
						break;
					}
					if (findSet(road[j][0]) != findSet(road[j][1])) {
						cnt += 1;
						amount += road[j][2];
						union(road[j][0], road[j][1]);
					}
				}
				sb.append((allcost - amount) + "\n");
				
			} 
				
		}
		
	}
	
	static int findSet(int x) {
		if (x == home[x]) {
			return x;
		} else {
			home[x] = findSet(home[x]);
			return home[x];
		}
	}
	
	static void union(int x, int y) {
		int px = findSet(x); int py = findSet(y);
		if (px != py) {
			if (px < py) {
				home[px] = py;
			} else {
				home[py] = px;
			}
		}
	}
}
