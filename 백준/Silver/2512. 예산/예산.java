import java.io.*;
import java.util.*;

public class Main {

    static int n, result;
    static int[] budget;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        budget = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            budget[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int limit = Integer.parseInt(st.nextToken());

        Arrays.sort(budget);

        binarySearch(limit);
        System.out.println(result);
    }


    static void binarySearch(int limit){

        int start = 1, end = budget[n - 1];


        while (start <= end) {
            int mid = (start + end) / 2;

            int amount = 0;

            for(int i = 0; i < n; i++){
                if(amount > limit){
                    break;
                }
                if(budget[i] > mid) {
                    amount += mid;
                } else {
                    amount += budget[i];
                }
            }

            if(amount > limit) {
                end = mid - 1;

            } else if(amount < limit) {
                result = mid;
                start = mid + 1;
            } else {
                result = mid;
                return;
            }
        }
    }
}
