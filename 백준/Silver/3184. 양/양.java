import java.io.*;
import java.util.*;

public class Main {
	
	static int r, c, sheep, wolf;
	static boolean[][] visited;
	static Character[][] arr;
	static int[] di = {0, 1, 0, -1}, dj = {1, 0, -1, 0};
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			r = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
		}
		
		arr = new Character[r][c];
		visited = new boolean[r][c];
		
		
		for (int i = 0; i < r; i++) {
			String line = br.readLine();
			for (int j = 0; j < c; j++) {
				arr[i][j] = line.charAt(j);
			}
		}
		
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (!arr[i][j].equals('#') && visited[i][j] == false) {
					int[] start = {i, j};
 					bfs(start);
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(sheep + " ");
		sb.append(wolf);
		System.out.println(sb);
		
	}
	
	static void bfs(int[] start) {
		ArrayDeque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		visited[start[0]][start[1]] = true;
		
		int innerSheep =0, innerWolf = 0;
		if (arr[start[0]][start[1]].equals('o')) {
			innerSheep += 1;
		} else if (arr[start[0]][start[1]].equals('v')) {
			innerWolf += 1;
		}
	
		while (!deq.isEmpty()) {
			int[] n = deq.pollFirst();
			for (int k = 0; k < 4; k++) {
				int ni = n[0] + di[k], nj = n[1] + dj[k];
				if (ni >= 0 && ni < r && nj >= 0 && nj < c && visited[ni][nj] == false && !arr[ni][nj].equals('#')) {
					if (arr[ni][nj].equals('o')) {
						innerSheep += 1;
					} else if (arr[ni][nj].equals('v')) {
						innerWolf += 1;
					}
					visited[ni][nj] = true;
					int[] tmp = {ni, nj}; 
					deq.add(tmp);
				}
			}
			
		}
		if (innerSheep != 0 && innerWolf != 0) {			
			if (innerSheep > innerWolf) {
				sheep += innerSheep;
			} else {
				wolf += innerWolf;
			}
		} else {
			sheep += innerSheep;
			wolf += innerWolf;
		}
	}
}
