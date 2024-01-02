import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static long[] checked;
    static long[] visited;
    static ArrayList<Integer>[] arr;
    static long sum;
    static long visitOrder;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        checked = new long[n + 1];
        visited = new long[n + 1];
        arr = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            arr[s].add(e);
            arr[e].add(s);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(arr[i]);
        }

        Arrays.fill(checked, -1);
        Arrays.fill(visited, 0);
        visitOrder = 1;
        dfs(start, 0);

        for (int i = 1; i < checked.length; i++) {
            if (checked[i] == -1) {
                continue;
            } else
                sum += checked[i] * visited[i];  // ti 대신에 visitOrder를 사용
//            System.out.println(sum);
        }
        System.out.println(sum);
    }

    private static void dfs(int node, long count) {
        checked[node] = count;
        visited[node] = visitOrder;

        for (int i : arr[node]) {
            if (checked[i] == -1) {
                visitOrder++;
                dfs(i, count + 1);
            }
        }
    }
}
