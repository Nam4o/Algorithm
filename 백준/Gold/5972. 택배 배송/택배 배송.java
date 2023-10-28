import java.io.*;
import java.util.*;

public class Main {
	
	static int n, m, current, next, c, node;
	static int[] start, now, cost, appnd;
	static List<int[]> graph[];
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}
		
		graph = new ArrayList[n + 1];
		
		for (int i = 0; i < n + 1; i++) {
			graph[i] = new ArrayList<int[]>();
		}
		
		cost = new int[n + 1];
		Arrays.fill(cost, Integer.MAX_VALUE);
		appnd = new int[2];
		
		for (int i = 0; i < m; i++) {
			
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			graph[a].add(new int[] {b, c});
			graph[b].add(new int[] {a, c});			
			
		}
		start = new int[2];
		start[0] = 0; start[1] = 1;
	
				
	System.out.println(dijkstra(start));
	}
	
	
	static int dijkstra(int[] start) {
		PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int []> (){
			@Override
			public int compare(int[] o1, int[] o2) {				
				return Integer.compare(o1[0], o2[0]);
			}
		});
		heap.add(start);
		cost[start[1]] = 0;
		
		while (!heap.isEmpty()) {
			now = heap.poll();
			current = now[0]; node = now[1];
			
			for (int i = 0; i < graph[node].size(); i++) {
				int[] tmp = graph[node].get(i);
				next = tmp[0];
				c = tmp[1];
				int newCost = current + c;
				if (cost[next] > newCost) {
					cost[next] = newCost;
					int[] nxt = {newCost, next};
					heap.add(nxt);
				}
				
			}
		}
		return cost[n];
	}
}