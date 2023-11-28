import java.io.*;
import java.util.*;


public class Main {
	
	static int n, m;
	static int [] parents;
	static int [][] relationship;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}
		
		parents = new int[n + 1];
		for (int i = 0; i <= n; i ++) {
			parents[i] = i;
		}
		
		relationship = new int[m][4];
		
		int amount = 0;
		
		for (int j = 0; j < m; j++) {
			st = new StringTokenizer(br.readLine());
			relationship[j][0] = Integer.parseInt(st.nextToken());
			relationship[j][1] = Integer.parseInt(st.nextToken());
			relationship[j][2] = Integer.parseInt(st.nextToken());
			relationship[j][3] = Integer.parseInt(st.nextToken());
			amount += relationship[j][2];
		}
		
		Arrays.sort(relationship, (o1, o2) -> o2[3] == o1[3]? o2[2] - o1[2] : o2[3] - o1[3]);
		
		int cnt = 1;
		int res = 0;
		
		for (int t = 0; t < m; t++) {
			if (cnt == n) {
				break;
			}
			if (relationship[t][3] == 1) {
				cnt += 1;
				res += relationship[t][2];
				union(relationship[t][0], relationship[t][1]);
			} else {
				if (findSet(relationship[t][0]) != findSet(relationship[t][1])) {
					cnt += 1;
					res += relationship[t][2];
					union(relationship[t][0], relationship[t][1]);
				}
			}
			
		}
		System.out.println(amount - res);
	}
	
	static int findSet(int x) {
		if (x == parents[x]) {
			return x;
		} else {
			parents[x] = findSet(parents[x]);
			return parents[x];
		} 
	}
	
	static void union(int x, int y) {
		int px = findSet(x), py = findSet(y);
		if (px != py) {
			if (px < py) {
				parents[px] = py;
			} else {
				parents[py] = px;
			}
		}
	}

}
