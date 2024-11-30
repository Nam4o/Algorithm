import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int k, n;
    static long result;
    static Integer[] lan;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        lan = new Integer[k];

        for(int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            lan[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(lan, Collections.reverseOrder());

        binarySearch();

        System.out.println(result);
    }

    public static void binarySearch() {

        long start = 1, end = lan[0];

        while (start <= end) {
            long mid = (start + end) / 2;
            int count = 0;
            for(int i = 0; i < k; i++) {
                if(lan[i] < mid){
                    break;
                } else {
                    count += lan[i] / mid;
                }
            }
            if(count < n) {
                end = mid - 1;
            } else {
                result = Math.max(result, mid);
                start = mid + 1;
            }
        }
    }
}
