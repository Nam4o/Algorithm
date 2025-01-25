import java.io.*;
import java.util.*;

public class Main {

    static int v, e;
    static int start, end, w;
    static int[][] graph;
    static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // V : 정점의 개수, E : 간선의 개수
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        
        graph = new int[e][3];
        parents = new int[v + 1];
        
        for(int i = 0; i <= v; i++) {
            parents[i] = i;
        }

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int[] container = new int[3];
            // start : 시작 정점, end : 도착 정점, w : 가중치
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            container[0] = start;
            container[1] = end;
            container[2] = w;
            graph[i] = container;
        }

        Arrays.sort(graph, (o1, o2) -> o1[2] - o2[2]);

        int cnt = 0, amount = 0;

        for(int[] info : graph) {
            if(findSet(info[0]) != findSet(info[1])) {
                cnt += 1;
                amount += info[2];
                union(info[0], info[1]);
            }
            if(cnt == v) {
                break;
            }
        }
        // 결과 출력
        System.out.println(amount);
        
    }
    
    // findSet
    public static int findSet(int x) {
        if(x == parents[x]) {
            return x;
        } else {
            parents[x] = findSet(parents[x]);
            return parents[x];
        }
    }
    
    // union
    public static void union(int x, int y) {
        int px = findSet(x), py = findSet(y);
        if(px != py) {
            if(px < py) {
                parents[py] = px;
            } else {
                parents[px] = py;
            }
        }
    }
}
