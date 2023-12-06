import java.io.*;
import java.util.*;

public class Main {
	
	static int t, i; 
	static int[] start, end;
	static int[][] board, visited;
	static int[] 
			di = {-1, -2, -2, -1, 1, 2, 2, 1},
			dj = {-2, -1, 1, 2, -2, -1, 1, 2};
			
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			i = Integer.parseInt(br.readLine());
			board = new int[i][i];
			visited = new int[i][i];
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			start = new int[2];
			end = new int[2];
			while (st.hasMoreTokens()) {
				start[0] = Integer.parseInt(st.nextToken());
				start[1] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				end[0] = Integer.parseInt(st.nextToken());
				end[1] = Integer.parseInt(st.nextToken());
			}
			System.out.println(bfs(start));
			
		}
		
	}
	
	static int bfs(int[] start) {
		ArrayDeque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		visited[start[0]][start[1]] = 1;
		
		
		while (!deq.isEmpty()) {
			int[] n = deq.pollFirst();
			if (n[0] == end[0] && n[1] == end[1]) {
				return visited[n[0]][n[1]] - 1;
				
				
			}
			for (int k = 0; k < 8; k++) {
				int ni = n[0] + di[k], nj = n[1] + dj[k];
				if (ni >= 0 && ni < i && nj >= 0 && nj < i && visited[ni][nj] == 0) {
					int[] tmp = {ni, nj};
					deq.add(tmp);
					visited[ni][nj] = visited[n[0]][n[1]] + 1;
					if (tmp[0] == end[0] && tmp[1] == end[1]) {
						return visited[ni][nj] - 1;
						
					}
				}
			}
 		}
		
		
		return -1;
		
	}
}
