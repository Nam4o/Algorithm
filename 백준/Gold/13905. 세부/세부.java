import java.util.*;
import java.io.*;

public class Main {
    public static int n, m, s, e;
    public static int[] parents;
    public static int[][] graph;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
        }

        graph = new int[m][3];
        parents = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int[] tmp = new int[3];
                graph[i][0] = Integer.parseInt(st.nextToken());
                graph[i][1] = Integer.parseInt(st.nextToken());
                graph[i][2] = Integer.parseInt(st.nextToken());
            }
        }
        int mx = Integer.MAX_VALUE;
        Arrays.sort(graph, ((o1, o2) -> o2[2] - o1[2]));

        boolean check = false;
        for (int i = 0; i < m; i++) {          
            if (findSet(graph[i][0]) != findSet(graph[i][1])) {
                if (graph[i][2] < mx) {
                    mx = graph[i][2];
                }
                union(graph[i][0], graph[i][1]);
            }
            if (findSet(s) == findSet(e)) {
                check = true;
                break;
            }
        }
        
        System.out.println(check == true?mx:0);
    }
    public static int findSet(int x) {
        if (x == parents[x]) {
            return x;
        } else {
            parents[x] = findSet(parents[x]);
            return parents[x];
        }
    }

    public static void union(int x, int y) {
        int px = findSet(x); int py = findSet(y);
        if (px != py) {
            if (px < py) {
                parents[py] = px;
            } else {
                parents[px] = py;
            }
        }
    }
}