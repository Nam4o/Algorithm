import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		Deque<Integer> deq = new LinkedList<>();
		
		for (int c = 0; c < n; c++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			ArrayList<Integer> command = new ArrayList<>();
			while (st.hasMoreTokens()) {
				int tmp = Integer.parseInt(st.nextToken());
				command.add(tmp);
				
			}
			if (command.size() == 2) {
				if (command.get(0).equals(1)) {
					deq.addFirst(command.get(1));
				} else {
					deq.addLast(command.get(1));
				}
			} else if (command.get(0).equals(3)) {
				if (!deq.isEmpty()) {
					writer.write(deq.pollFirst() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			} else if (command.get(0).equals(4)) {
				if (!deq.isEmpty()) {
					writer.write(deq.pollLast() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			} else if (command.get(0).equals(5)) {
				writer.write(deq.size() + "\n");
			} else if (command.get(0).equals(6)) {
				if (!deq.isEmpty()) {
					writer.write(0 + "\n");
				} else {
					writer.write(1 + "\n");
				}
			} else if (command.get(0).equals(7)) {
				if (!deq.isEmpty()) {
					writer.write(deq.getFirst() + "\n");
				} else {
					writer.write(-1 + "\n");
				}
			} else {
				if (!deq.isEmpty()) {
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
