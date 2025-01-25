import java.io.*;
import java.util.*;

public class Main {

    static int n, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n : 물품의 수, k : 버틸 수 있는 무게
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[][] memo = new int[k + 1][n + 1];
        int[][] items = new int[n + 1][2];
        // row : 각 무게 단계마다 배낭에 넣을 수 있는 최대 가치
        // col : 각 물품의 순서마다 이전과 비교해서 배낭에 넣을 지 판단

        for(int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            // w : 물품의 무게, v : 물품의 가치
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            items[i] = new int[]{w, v};
        }

        for(int i = 1; i <= k; i++) {
            for(int j = 1; j <= n; j++) {
                // memo의 현재 가방 최대 무게가 items의 현재 item의 무게 이하라면
                if(i >= items[j][0]) {
                    // 현재 아이템을 뺀 가방의 무게에서 가질 수 있는 최대 가치를 더한 값과
                    // 현재 아이템의 가치 중 더 큰 것을 갱신
                    memo[i][j] = Math.max(memo[i][j - 1], items[j][1] + memo[i - items[j][0]][j - 1]);
                } else if (i < items[j][0]) {
                    memo[i][j] = memo[i][j - 1];
                }
            }
        }
        System.out.println(memo[k][n]);
    }
}
