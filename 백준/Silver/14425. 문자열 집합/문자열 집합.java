import java.util.*;
import java.io.*;


public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		
		ArrayList<String> base = new ArrayList();
		
		for (int i = 0; i < N; i++) {
			base.add(br.readLine());
		}
		
		int cnt = 0;
		
		for (int j = 0; j < M; j++) {
			String word = br.readLine();
			if (base.contains(word)) {
				cnt += 1;
			}
		}
		writer.write(cnt + "");
		writer.flush();
		
	}
}
