import java.io.*;
import java.util.*;



public class Main {
	static String[][] stairs;
	static int[][][] visited;
	static int l;
	static int r;
	static int c;
	static int[] di = {0, 1, 0, -1};
	static int[] dj = {1, 0, -1, 0};
	static int[] start = new int[3];
	static int[] end = new int[3];
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		l = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		while (l != 0) {
			
			stairs = new String[r][c];
			visited = new int[l][r][c];
			for (int ln = 0; ln < l; ln++) {
				for (int i = 0; i < r; i++) {
					String line = br.readLine();
					
					for (int j = 0; j < c; j++) {
						stairs[i][j] = String.valueOf(line.charAt(j));
						switch (stairs[i][j]) {
						case "S" : start[0] = ln; start[1] = i; start[2] = j; visited[ln][i][j] = 1; break;
						case "E" : end[0] = ln; end[1] = i; end[2] = j; break;
						case "." : visited[ln][i][j] = 0; break;
						case "#" : visited[ln][i][j] = -1; break;
						}
					}
				}
				String blank = br.readLine();
			}
			bfs(start);
            
			StringBuilder sb = new StringBuilder();
			if (visited[end[0]][end[1]][end[2]] == 0) {
				sb.append("Trapped!");
			} else {
				sb.append("Escaped in ");
				sb.append(visited[end[0]][end[1]][end[2]] - 1);
				sb.append(" minute(s).");
			}
			System.out.println(sb);
            
		st = new StringTokenizer(br.readLine());
		l = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		}	
		
	}
	
	static void bfs(int[] start) {
		Deque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		
		while (!deq.isEmpty()) {
			int[] n = deq.pollFirst();
			for (int k = 0; k < 4; k++ ) {
				int nln = n[0];
				int ni = n[1] + di[k];
				int nj = n[2] + dj[k];
				if (0 <= ni && ni < r && 0 <= nj && nj < c && visited[nln][ni][nj] == 0) {
					visited[nln][ni][nj] = visited[n[0]][n[1]][n[2]] + 1;
					int[] tmp = {nln, ni, nj};
					deq.add(tmp);
					
				}
			
				if (n[0] + 1 < l && visited[n[0] + 1][n[1]][n[2]] == 0) {
					visited[n[0] + 1][n[1]][n[2]] = visited[n[0]][n[1]][n[2]] + 1;
					int[] tmp2 = {n[0] + 1, n[1], n[2]};
					deq.add(tmp2);					
				} else if (n[0] - 1 >= 0 && visited[n[0] - 1][n[1]][n[2]] == 0) {
					visited[n[0] - 1][n[1]][n[2]] = visited[n[0]][n[1]][n[2]] + 1;
					int[] tmp2 = {n[0] - 1, n[1], n[2]};
					deq.add(tmp2);
				}
			
			} 
		}
	}
}
