import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			int n = Integer.parseInt(br.readLine());
			
			Deque<String> cards = new LinkedList<>();
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				String card = st.nextToken();
				
				if (cards.isEmpty() == true) {
					
					cards.add(card);
				} else {
					Character a = cards.getFirst().charAt(0);
					Character b = cards.getLast().charAt(0);
					Character c = card.charAt(0);
					if (c <= a) {
						cards.addFirst(card);
					} else {
						cards.addLast(card);
					}
					
				}
				
			}
			String answer = String.join("", cards);
			
			writer.write(answer + "\n");
			
		}
		writer.flush();
		writer.close();
	}
}
