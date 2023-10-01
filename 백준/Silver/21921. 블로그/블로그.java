import java.util.*;
import java.io.*;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Queue<Integer> q = new LinkedList<>();
		
		int n = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		
		String arr = br.readLine();

		String [] list = arr.split(" ");
		
		int max_visit = 0;
		int days = 1;
		int now_visit = 0;
		
		for (int j = 0; j < x; j++) {
			int tmp = Integer.parseInt(list[j]);
			q.add(tmp);
			max_visit += tmp;
			now_visit += tmp;
		}
		

		for (int i = x; i < n; i++) {
			int r = q.poll();
			now_visit -= r;
			int tmp2 = Integer.parseInt(list[i]);
			q.add(tmp2);
			now_visit += tmp2;

			if (now_visit > max_visit) {
				max_visit = now_visit;
				days = 1;
			} else if (now_visit == max_visit) {
				days += 1;
			}
		}
		if (max_visit == 0) {
			writer.write("SAD");
			writer.flush();
		} else {
			writer.write(max_visit + "\n" + days);
			writer.flush();
		}
	}
}
