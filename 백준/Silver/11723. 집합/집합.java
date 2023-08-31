import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean[] S = new boolean[21];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int value = 0;

            if (st.hasMoreTokens()) {
                value = Integer.parseInt(st.nextToken());
            }

            switch (command) {
                case "add":
                    S[value] = true;
                    break;
                case "remove":
                    S[value] = false;
                    break;
                case "check":
                    sb.append(S[value] ? 1 : 0).append('\n');
                    break;
                case "toggle":
                    S[value] = !S[value];
                    break;
                case "all":
                    for (int j = 0; j <= 20; j++) {
                        S[j] = true;
                    }
                    break;
                case "empty":
                    for (int j = 0; j <= 20; j++) {
                        S[j] = false;
                    }
                    break;
            }
        }

        System.out.println(sb);
    }
}
