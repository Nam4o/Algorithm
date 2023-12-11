import java.io.*;
import java.util.*;

public class Main {

    static int t, n;
    static String cloth, sep;


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        t = Integer.parseInt(br.readLine());


        StringBuilder sb = new StringBuilder();

        for (int tc = 0; tc < t; tc++) {
            n = Integer.parseInt(br.readLine());
            HashMap<String, ArrayList<String>> clothes = new HashMap<>();
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                while (st.hasMoreTokens()) {
                    cloth = st.nextToken();
                    sep = st.nextToken();
                }
                if (clothes.containsKey(sep)) {
                    clothes.get(sep).add(cloth);
                } else {
                    ArrayList<String> tmp = new ArrayList<>();
                    tmp.add(cloth);
                    clothes.put(sep, tmp);
                }
            }
            int ans = 1;
            for (String clth:clothes.keySet()) {
                ans *= clothes.get(clth).size() + 1;
            }
            if (t == tc - 1){
                sb.append(ans - 1);
            } else {
                sb.append(ans - 1 + "\n");
            }
        }
        System.out.println(sb);
    }
}
