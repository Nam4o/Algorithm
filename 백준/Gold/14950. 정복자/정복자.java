
import java.io.*;
import java.util.*;

public class Main {

    static int n, m, t;
    static int[] parents;
    static int[][] connects;

    public static void main(String[] args) throws IOException{
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
        }
        connects = new int[m][3];
        parents = new int[n + 1];
        for (int j = 1; j <= n; j++) {
            parents[j] = j;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                connects[i][0] = Integer.parseInt(st.nextToken());
                connects[i][1] = Integer.parseInt(st.nextToken());
                connects[i][2] = Integer.parseInt(st.nextToken());
            }

        }

        Arrays.sort(connects, (o1, o2) -> o1[2] - o2[2]);

        int cnt = 1;
        long amount = 0;
        for (int w = 0; w < m; w++) {
            if (cnt == n) {
                break;
            }
            if (findSet(connects[w][0]) != findSet(connects[w][1])) {

                amount += connects[w][2] + t * (cnt - 1);
                cnt += 1;
                union(connects[w][0], connects[w][1]);
            }
        }
        System.out.println(amount);
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
        int px = findSet(x), py = findSet(y);
        if (px != py) {
            if (px < py) {
                parents[px] = py;
            } else {
                parents[py] = px;
            }
        }
    }
}