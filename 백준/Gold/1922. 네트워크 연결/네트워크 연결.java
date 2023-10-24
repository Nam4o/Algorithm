import java.io.*;
import java.util.*;

public class Main {
    
    static int n, m, cnt, amount;
    static int[] parents;
    static int[][] graph;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
    
        
        parents = new int[n + 1];
        for (int p = 1; p < n + 1; p++) {
        	parents[p] = p;
        }
        graph = new int[m][3];
        
        for (int connect = 0; connect < m; connect++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                graph[connect][0] = Integer.parseInt(st.nextToken());
                graph[connect][1] = Integer.parseInt(st.nextToken());
                graph[connect][2] = Integer.parseInt(st.nextToken());    
            }
        
        }
        Arrays.sort(graph, (o1, o2) -> { return o1[2] - o2[2];});
        
        for (int i = 0; i < m; i++) {
            if (cnt == n) {
                break;
            }
            if (findSet(graph[i][0]) != findSet(graph[i][1])) {
                cnt += 1;
                amount += graph[i][2];
                union(graph[i][0], graph[i][1]);
            }
        }
        sb.append(amount);
        System.out.println(sb);
    }
    
    static int findSet(int x) {
        if (x == parents[x]) {
            return x;
        } else {
            parents[x] = findSet(parents[x]);
            return parents[x];
        }
    }
    
    static void union(int x, int y) {
        int px = findSet(x);
        int py = findSet(y);
        if (px != py) {
            if (px < py) {
                parents[px] = py;
            } else {
                parents[py] = px;
            }
        }
        
    }

}
