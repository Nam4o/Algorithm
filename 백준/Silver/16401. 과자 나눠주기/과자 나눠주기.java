import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    static int m, n;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        
        Integer[] snacks = new Integer[n];
        
        for(int i = 0; i < n; i++) {
            int snackLength = Integer.parseInt(st.nextToken());
            snacks[i] = snackLength;
        }

        Arrays.sort(snacks, Collections.reverseOrder());

        int start = 1, end = snacks[0];

        int result = 0;
        while (start <= end ) {
            int mid = (start + end) / 2;
            int count = 0;
            for(Integer i : snacks) {
                if(i >= mid) {
                    count += i / mid;
                }

            }
            if(count < m){
                end = mid - 1;
            } else {
                start = mid + 1;
                result = mid;
            }
        }
        System.out.println(result);
    }
}