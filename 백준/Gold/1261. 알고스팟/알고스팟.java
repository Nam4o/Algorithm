import java.io.*;
import java.util.*;

public class Main {
    static int m, n, nx, ny, ni, nj, current;
    static int[][] arr;
    static boolean[][] visited;
    static int[] tmp, start = new int[3];
    static int[] di = {0, -1, 0, 1};
    static int[] dj = {-1, 0, 1, 0};    
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
        }
        arr = new int [n][m];
        visited = new boolean [n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }
        System.out.println(dijkstra(0,0));
    }

    static int dijkstra(int si, int sj) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
        	@Override
        	public int compare(int[] o1, int[] o2) {
        		return Integer.compare(o1[0], o2[0]);
        	}
        });
        start[0] = 0; start[1] = si; start[2] = sj;
        heap.add(start);
        visited[si][sj] = true;
        
        while (!heap.isEmpty()) {
            tmp = heap.poll();
            current = tmp[0]; nx = tmp[1]; ny = tmp[2];
            if (nx == n -1 && ny == m - 1) {
                return current;
            }
            for (int k = 0; k < 4; k++) {
                ni = nx + di[k]; nj = ny + dj[k];
                if (0 <= ni && ni < n && 0 <= nj && nj < m && !visited[ni][nj]) {
                    if (arr[ni][nj] == 1) {
                        int[] next = new int[3];
                        next[0] = current + 1; next[1] = ni; next[2] = nj;
                        heap.add(next);
                        visited[ni][nj] = true;
                    } else {
                        int[] next = new int[3];
                        next[0] = current; next[1] = ni; next[2] = nj;
                        heap.add(next);
                        visited[ni][nj] = true;
                    }  
                }
            }
        }
        return -1;
    }
}