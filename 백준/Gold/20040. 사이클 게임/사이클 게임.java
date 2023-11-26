import java.io.*;
import java.util.*;

public class Main {
	
	static int n, m, p1, p2, cnt, check;
	static int [] point;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken()); 
			m = Integer.parseInt(st.nextToken());
		}
		
		point = new int [n];
		
		for (int j = 0; j < n; j++) {
			point[j] = j;
		}
		
		check = 1;
		
		boolean isCheck = false;
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				p1 = Integer.parseInt(st.nextToken());
				p2 = Integer.parseInt(st.nextToken());
			}
			cnt += 1;
			if (findSet(p1) != findSet(p2)) {
				union(p1, p2);
			} else {
				System.out.println(cnt);
				isCheck = true;
				break;
			}					
		}
		if (isCheck == false) {
			System.out.println(0);
		}
		
				
	}
	static int findSet(int x) {
		if (x == point[x]) {
			return x;
		} else {
			point[x] = findSet(point[x]);
			return point[x];
		}
	}
	
	static void union(int x, int y) {
		int px = findSet(x); int py = findSet(y);
		
		if (px != py) {
			if (px < py) {
				point[px] = py;
			} else {
				point[py] = px;
			}
		}
	}
	
}
