import java.io.*;
import java.util.*;

public class Main {
	
	static int w, h, cnt;
	static int[][] island;
	static int[] di = {0, 1, 0, -1, 1, -1, 1, -1};
	static int[] dj = {1, 0, -1, 0, 1, 1, -1, -1};
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				w = Integer.parseInt(st.nextToken());
				h = Integer.parseInt(st.nextToken());
			}
			if (w == 0 && h == 0) {
				break;
			} else {
				cnt = 0;
				island = new int[h][w];
				visited = new boolean[h][w];
			
				
				for (int i = 0; i < h; i++) {
					st = new StringTokenizer(br.readLine());
					for (int j = 0; j < w; j++) {
						island[i][j] = Integer.parseInt(st.nextToken());
					}
				}
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					if (island[i][j] == 1 && visited[i][j] == false) {
						int[] start = {i, j};
						bfs(start);
					}
				}
			}
			sb.append(cnt + "\n");
			
			}
			
		}
		System.out.println(sb);
		
		
	}
	
	static void bfs(int[] start) {
		ArrayDeque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		visited[start[0]][start[1]] = true;
		
		while (!deq.isEmpty()) {
			int[] n = deq.pollFirst();
			for (int k = 0; k < 8; k++) {
				int ni = n[0] + di[k];
				int nj = n[1] + dj[k];
				if (ni >= 0 && ni < h && nj >= 0 && nj < w && visited[ni][nj] == false && island[ni][nj] == 1) {
					int[] tmp = {ni, nj};
					deq.add(tmp);
					visited[ni][nj] = true;
				}
			}
		}
		cnt += 1;
	}

}
