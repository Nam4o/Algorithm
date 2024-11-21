import java.io.*;
import java.util.*;

public class Main {
    static int n, mx;
    static int[] di = new int[] {0, 1, 0, -1};
    static int[] dj = new int[] {1, 0, -1, 0};
    static int[][] arr;
    static boolean[][] check;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n][n];

        check = new boolean[n][n];


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
//                System.out.println(arr[i][j]);
            }
        }
        if(n == 1) {
            System.out.println(0);
        } else {
            dijkstra();
            System.out.println(mx);
        }
    }

    public static void dijkstra() {

        PriorityQueue<Q> queue = new PriorityQueue<>();
        queue.add(new Q(0, 0, 0));

        while (!queue.isEmpty()) {
            Q prevInfo = queue.poll();
            check[prevInfo.x][prevInfo.y] = true;
            int[] node = new int[] {prevInfo.x, prevInfo.y};
            mx = Math.max(mx, prevInfo.num);
            if(node[0] == n - 1 && node[1] == n - 1) {
                return;
            }
            for(int k = 0; k < 4; k++) {
                int[] nextNode = new int[] {node[0] + di[k], node[1] + dj[k]};
                if((nextNode[0] < n && 0 <= nextNode[0]) && (nextNode[1] < n && 0 <= nextNode[1]) && check[nextNode[0]][nextNode[1]] == false) {
                    queue.add(new Q(nextNode[0], nextNode[1], Math.abs(arr[node[0]][node[1]] - arr[nextNode[0]][nextNode[1]])));
                }
            }
        }
    }
    static class Q implements Comparable<Q> {
        int x;
        int y;
        int num;

        @Override
        public int compareTo(Q o) {
            if(o.num < this.num) {
                return 1;
            } else {
                return -1;
            }
        }

        public Q(int x, int y, int num) {
            this.x = x;
            this.y = y;
            this.num = num;
        }
    }
}