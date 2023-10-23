import java.util.*;

import java.io.*;

public class Main { 
    
    static int n, m, k, x, y;
    static int[] connect = new int[3];
    static int[] parents, ans;
    static int[][] graph;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringBuilder sb = new StringBuilder();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
        }
        
        graph = new int[m + 1][3];
        
        parents = new int[m + 1];
        
        ans = new int[k];
        
        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
            graph[i - 1][0] = Integer.parseInt(st.nextToken());
            graph[i - 1][1] = Integer.parseInt(st.nextToken());
            }
            graph[i - 1][2] = i;
             
        }

        for (int j = 0; j < k; j++) {
        	for (int i = 1; i < m + 1; i++) {
                parents[i] = i;
            }
            int cnt = 0; int amount = 0;
            for (int w = j; w < m; w++) {
                if (cnt == n) {
                	sb.append(amount);
                	break;
                }
                if (findSet(graph[w][0]) != findSet(graph[w][1])) {              	    
                	cnt += 1;
                	amount += graph[w][2];
                	union(graph[w][0], graph[w][1]);
                }
            }

            if (cnt == n - 1) {
            sb.append(amount + " ");
            } else if (cnt < n - 1) {
            	sb.append(0 + " ");
            }
        }

        sb.deleteCharAt(sb.length() - 1);
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