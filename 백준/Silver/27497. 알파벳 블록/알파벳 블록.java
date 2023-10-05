import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		Deque<String> deq = new LinkedList<>();
		ArrayList<ArrayList> arr = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			ArrayList<String> tmp = new ArrayList<String>();
			while (st.hasMoreTokens()) {
				String a = st.nextToken();
				tmp.add(a);
				
			}
			
			if (tmp.get(0).equals("3")) {
				if (arr.isEmpty() == false) {
					arr.remove(arr.size() - 1);
				} else {
					continue;
				}
			} else {
				arr.add(tmp);
			}
		
		}
		if (!arr.isEmpty()) {
			for (int j = 0; j < arr.size(); j++) {
				String insrt = String.valueOf(arr.get(j).get(1));
				if (arr.get(j).get(0).equals("1")) {
					deq.addLast(insrt);
				} else {
					deq.addFirst(insrt);
				}	
			}
		}
		
		if (!deq.isEmpty()) { 
			while (!deq.isEmpty()){
				writer.write(deq.pollFirst() + "");
				
			}
		} else {
			writer.write(0 + "\n");
			
		}
	writer.flush();
	writer.close();
	}
}
