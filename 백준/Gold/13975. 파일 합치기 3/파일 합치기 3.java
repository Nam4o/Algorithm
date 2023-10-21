import java.io.*;
import java.util.*;

public class Main {
	
	static int t, k;
	static long cost, p1, p2, p3;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			k = Integer.parseInt(br.readLine());

			PriorityQueue<Long> heap = new PriorityQueue<>();
			
			StringTokenizer st = new StringTokenizer(br.readLine());	
			
			cost = 0;
			
			for (int i = 0; i < k; i++) {
				heap.add(Long.parseLong(st.nextToken()));
			}
			while (heap.size() != 1) {
				p1 = heap.poll(); p2 = heap.poll();
				p3 = p1 + p2;
				cost += p3;
				heap.add(p3);		
			}
			sb.append(cost + "\n");
		}
		System.out.println(sb);
	}
}
