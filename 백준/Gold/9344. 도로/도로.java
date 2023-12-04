import java.io.*;
import java.util.*;

public class Main {

    static int t, n, m, p, q;
    static int[] parents;
    static int[][] info;
    static boolean check;


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                n = Integer.parseInt(st.nextToken());
                m = Integer.parseInt(st.nextToken());
                p = Integer.parseInt(st.nextToken());
                q = Integer.parseInt(st.nextToken());
            }
            parents = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parents[i] = i;
            }
            info = new int[m][3];
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                while (st.hasMoreTokens()) {
                    info[i][0] = Integer.parseInt(st.nextToken());
                    info[i][1] = Integer.parseInt(st.nextToken());
                    info[i][2] = Integer.parseInt(st.nextToken());
                }
            }
            Arrays.sort(info, (o1, o2) -> o1[2] - o2[2]);

            boolean check = false;
            int cnt = 1;

            for (int i = 0; i < m; i++) {
                if (cnt == n) {
                    break;
                }
                if (findSet(info[i][0]) != findSet(info[i][1])) {
                    cnt += 1;
                    union(info[i][0], info[i][1]);
                    if ((info[i][0] == p && info[i][1] == q) || (info[i][0] == q && info[i][1] == p)) {
                        check = true;
                    }
                }
            }
            if (check && cnt == n) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

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
