import java.util.*;
import java.io.*;



public class Main {
	static int n, k, s, x, y;
	static int[][] arr, visited;
	static int[] di = {0, 1, 0, -1}; 
	static int[] dj = {1, 0, -1, 0};
	static int[] start;
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
		}
		
		arr = new int[n][n];
		visited = new int[n][n];
		
		ArrayList<int[]> list = new ArrayList<>();
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] != 0) {
					start = new int[3];
					start[0] = i;
					start[1] = j;
					start[2] = arr[i][j];
					list.add(start);
				}
			}
		}
		
		Collections.sort(list, (o1, o2) -> {return o1[2] - o2[2];});
		
		st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			s = Integer.parseInt(st.nextToken());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(bfs(list));

		System.out.println(sb);	
	}
	
	
	static int bfs(ArrayList<int[]> list) {
		Deque<int[]> deq = new ArrayDeque<>();
		
		for (int ln = 0; ln < list.size(); ln++) {
			int[] tmp = list.get(ln);
			int a = tmp[0];
			int b = tmp[1];
			int c = tmp[2];
			visited[a][b] = 1;
			int[] virus = {a, b, c, 0};
			deq.add(virus);
		}
		
		while (!deq.isEmpty()) {
			int[] node = deq.pollFirst();
			if (node[3] == s) {
				if (node[0] == x - 1 && node[1] == y - 1) {
					return node[2];
				}
			} else if (node[3] < s) {
				if (arr[x - 1][y - 1] != 0) {
					return arr[x - 1][y - 1];
				}
			} else {
				return 0;
			}
			for (int k = 0; k < 4; k++) {
				int ni = node[0] + di[k]; 
				int nj = node[1] + dj[k];
				if (0 <= ni && ni < n && 0 <= nj && nj < n && visited[ni][nj] == 0 && arr[ni][nj] == 0) {
					visited[ni][nj] = 1;
					arr[ni][nj] = arr[node[0]][node[1]];
					int[] virus = {ni, nj, node[2], node[3] + 1};
					deq.add(virus);
				}
			}
		}
		
	return 0;	
	
	}

}
