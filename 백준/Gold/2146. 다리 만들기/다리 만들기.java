import java.io.*;
import java.util.*;

public class Main {
	
	static int[][] arr, visited;
	static int[] di = {1, 0, -1, 0}, dj = {0, 1, 0, -1}, tmp;
	static int cnt = 1;	
	static int n, x, y, nx, ny, mn;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		n = Integer.parseInt(br.readLine());
		
		arr = new int[n][n];
		visited = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					visited[i][j] = 0;
			}	
		}
		
		for (int q = 0; q < n; q++) {
			for (int p = 0; p < n; p++) {
				if (visited[q][p] == 0 && arr[q][p] == 1) {
					int[] start = {q, p};
					bfs(start);
				}
			}
		}

		mn = 9999999;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (visited[i][j] != 0) {
					int[] start = {i, j};
					int res = bridge(start, visited[i][j]);
					if (res != -1 && res < mn) {
						mn = bridge(start, visited[i][j]);
					} else {
						continue;
					}
				}
			}
		}
		sb.append(mn - 2);
		System.out.println(sb);
	}
	
    
	static void bfs(int[] start) {
		Deque<int[]> deq = new ArrayDeque<>();
		
		deq.add(start);
		visited[start[0]][start[1]] = cnt;
		
		while (!deq.isEmpty()) {
			tmp = deq.pollFirst();
			x = tmp[0]; y = tmp[1];
			
			for (int k = 0; k < 4; k++) {
				nx = x + di[k]; ny = y + dj[k];
				if (0 <= nx && nx < n && 0 <= ny && ny < n && visited[nx][ny] == 0 && arr[nx][ny] == 1) {
					int[] inner = {nx, ny};
					deq.add(inner);
					visited[nx][ny] = cnt;
				}
			}
		}
		cnt += 1;
	}
	
	static int bridge(int[] start, int me) {
		Deque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		int[][] check = new int[n][n];
		check[start[0]][start[1]] = 1;
		
		while (!deq.isEmpty()) {
			tmp = deq.pollFirst();
			x = tmp[0]; y = tmp[1];
			
			if (visited[x][y] != 0 && visited[x][y] != me) {
				return check[x][y];
			}
			for (int k = 0; k < 4; k++) {
				nx = x + di[k]; ny = y + dj[k];
				if (0 <= nx && nx < n && 0 <= ny && ny < n && check[nx][ny] == 0 && visited[nx][ny] != me) {
					int[] inner = {nx, ny};
					deq.add(inner);
					check[nx][ny] = check[x][y] + 1;
				}
			}
		}
		return -1;
	}
}
