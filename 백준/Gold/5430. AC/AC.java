import java.util.*;
import java.io.*;

public class Main {
	static int t;
	static String cmd;
	static int n;
	static String given;
	static boolean isReverse;
	static boolean isPossibe;
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc ++) {
			isReverse = false;
			isPossibe = true;
			
			cmd = br.readLine();
			n = Integer.parseInt(br.readLine());
			Deque<String> deq = new ArrayDeque<>();
			given = br.readLine();
			
			if (n != 0) {
				given = given.substring(1, given.length() - 1);
				String[] arr = given.split(",");
				
				for (String str: arr) {
					deq.add(str);
				}
				
			}
			
	
			for (int i = 0; i < cmd.length(); i++) {
				if (cmd.charAt(i) == 'R') {
					if (isReverse == false) {
						isReverse = true;
					} else {
						isReverse = false;
					}
				} else {
					if (deq.isEmpty()) {
						isPossibe = false;
					} else {
						if (isReverse == false) {
							deq.pollFirst();
						} else {
							deq.pollLast();
						}						
					}
				}
			}
			int sz = deq.size();
			
			if (isPossibe) {
				if (deq.isEmpty()) {
					sb.append("[]"+"\n");
				}else if (sz == 1) {
					sb.append("[" + deq.pollFirst() + "]" + "\n");
				}
				else {
					if (isReverse == false) {						
						while (!deq.isEmpty()) {
							if (deq.size() == 1) {
								sb.append(deq.pollFirst() + "]" + "\n");
							} else if (deq.size() == sz) { 
								sb.append("[" + deq.pollFirst() + ",");
							}else {
								sb.append(deq.pollFirst() + ",");
							}
							
						}
					} else {
						if (sz != 1) {
							while (!deq.isEmpty()) {
								if (deq.size() == 1) {
									sb.append(deq.pollLast() + "]" + "\n");
								} else if (deq.size() == sz) { 
									sb.append("[" + deq.pollLast() + ",");
								}else {
									sb.append(deq.pollLast() + ",");
								}	
						}
						} 
					}				
				}
				
			} else {
				sb.append("error" + "\n");
			}

		}
		System.out.println(sb);
	}
}


