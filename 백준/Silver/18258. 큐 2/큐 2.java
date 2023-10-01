import java.util.*;
import java.io.*;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		Deque<Integer> deq = new ArrayDeque<>();
		
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			ArrayList<String> command = new ArrayList<>();
			
			while (st.hasMoreTokens()) {
			String a = st.nextToken();
			command.add(a);
			}
			
			
			if (command.get(0).equals("push")) {
				deq.add(Integer.parseInt(command.get(1)));
			} else if (command.get(0).equals("pop")) {
				if (deq.isEmpty() == false) {
					writer.write(deq.pollFirst() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			} else if (command.get(0).equals("size")) {
				writer.write(deq.size() + "\n");
			} else if (command.get(0).equals("empty")) {
				if (deq.isEmpty() == true) {
					writer.write(1 + "\n");
				} else {
					writer.write(0 + "\n");
				}
			} else if (command.get(0).equals("front")) {
				if (deq.isEmpty() == false) {
					writer.write(deq.getFirst() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			} else if (command.get(0).equals("back")) {
				if (deq.isEmpty() == false) {
					writer.write(deq.getLast() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			}
		}
	writer.flush();
	writer.close();
	}
}
