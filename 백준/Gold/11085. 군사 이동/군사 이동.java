import java.util.*;
import java.io.*;

public class Main {
	static int p, w, c, v, mn;
	static int[] parents;
	static int[][] roads;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			p = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
		}
		
		roads = new int[w][3];
		parents = new int[p];
		for (int prt = 0; prt < p; prt++) {
			parents[prt] = prt;
		}
		
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			c = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < w; i++) {
			st = new StringTokenizer(br.readLine());
			roads[i][0] = Integer.parseInt(st.nextToken());
			roads[i][1] = Integer.parseInt(st.nextToken());
			roads[i][2] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(roads, (o1, o2) -> {return o2[2] - o1[2];});

		mn = Integer.MAX_VALUE;

		for (int j = 0; j < w; j++) {
			if (findSet(c) == findSet(v)) {
				break;
			} else {
				if (findSet(roads[j][0]) != findSet(roads[j][1])) {
					union(roads[j][0], roads[j][1]);
					if (roads[j][2] < mn) {
						mn = roads[j][2];
					}
				}
			}
		}
		System.out.println(mn);
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
		int px = findSet(x);
		int py = findSet(y);
		if (px != py) {
			if (px < py) {
				parents[px] = py;
			} else {
				parents[py] = px;
			}
		}
	}
}
