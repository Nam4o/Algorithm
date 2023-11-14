import java.util.*;
import java.io.*;

public class Main {
	static int m, n, k, xs, xe, ys, ye;
	static int[] start, now;
	static int[][] arr, visited;
	static ArrayList<Integer> list = new ArrayList<>();
	
	static int[] di = {0, 1, 0, -1};
	static int[] dj = {1, 0, -1, 0};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		while (st.hasMoreTokens()) {
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
		}
		arr = new int[m][n];
		visited = new int[m][n];
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			xs = Integer.parseInt(st.nextToken());
			ys = Integer.parseInt(st.nextToken());
			xe = Integer.parseInt(st.nextToken());
			ye = Integer.parseInt(st.nextToken());
			for (int x = xs; x < xe; x++) {
				for (int y = ys; y < ye; y++) {
					if (arr[y][x] == 0) {
						arr[y][x] = 1;
					}
					
				}
			}
		}
		start = new int[2];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (arr[i][j] == 0 && visited[i][j] == 0) {
					start[0] = i; start[1] = j;
					bfs(start);
				}
			}
		}
		Collections.sort(list);
		StringBuilder sb = new StringBuilder();
		for (int t = 0; t < list.size(); t++) {
			if (t != list.size() - 1) {
			sb.append(list.get(t) + " ");
			} else {
			sb.append(list.get(t));
			}
		}
        System.out.println(list.size());
		System.out.println(sb);
	}
	
	static void bfs(int[] start) {
		Deque<int[]> deq = new ArrayDeque<>();
		deq.add(start);
		visited[start[0]][start[1]] = 1;
		int cnt = 1;
		
		while (!deq.isEmpty()) {
			now = deq.pollFirst();
			for (int i = 0; i < 4; i++) {
				int ni = now[0] + di[i];
				int nj = now[1] + dj[i];
				if (ni >= 0 && ni < m && nj >= 0 && nj < n && visited[ni][nj] == 0 && arr[ni][nj] == 0) {
					int[] tmp = {ni, nj}; 
					deq.add(tmp);
					visited[ni][nj] = visited[now[0]][now[1]] + 1;
					cnt += 1;
				}
			}
		}
		
		list.add(cnt);
	
	}

}
