import java.io.*;
import java.util.*;

public class Main {
	static int n, m;
	static int[] info = new int[3];
	static int[][] arr;
	static int[] parents;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}
		
		arr = new int[m][3];
		
		parents = new int[n + 1]; 
		for (int p = 1; p < n + 1; p ++) {
			parents[p] = p;
		}
		
		long amount = 0;
		
		for (int way = 0; way < m; way++) {
			st = new StringTokenizer(br.readLine());
			for (int v = 0; v < 3; v++) {
				info[v] = Integer.parseInt(st.nextToken());
				arr[way][v] = info[v];
				if (v == 2) {
					amount += info[v];
				}
			}
		}
		Arrays.sort(arr, (o1, o2) -> { return o1[2] - o2[2];});
		
		int cnt = 1;
		long ans = 0;
		for (int i = 0; i < m; i++) {
			if (cnt == n) {
				break;
			} else {
				if (findset(arr[i][0]) != findset(arr[i][1])) {
					cnt += 1;
					ans += arr[i][2];
					union(arr[i][0], arr[i][1]);
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		if (cnt == n) {
			sb.append(amount - ans);
		} else {
			sb.append(-1);
		}
		System.out.println(sb);			
	}
	
	static int findset(int x) {
		if (x == parents[x]) {
			return x;			
		} else {
			parents[x] = findset(parents[x]);
			return parents[x];	
		}
	}
	
	static void union(int x, int y) {
		int px = findset(x); int py = findset(y);
		if (px != py) {
			if (px < py) {
				parents[px] = py;
			} else {
				parents[py] = px;
			}
		}
	}
	
}
