import java.io.*;
import java.util.*;

public class Main {
	
	public static int tmp;
	public static boolean check;
	
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		ArrayList<Integer> numb = new ArrayList<>();
		ArrayList<String> oper = new ArrayList<>();
		
		String line = br.readLine();
		int inputSize = line.length();
		
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < inputSize; i++) {
			if (line.charAt(i) != '+' && line.charAt(i) != '-') {
				sb.append(line.charAt(i));
				if (i == (inputSize - 1)) {
					numb.add(Integer.parseInt(sb.toString()));
				}
			} else {
				numb.add(Integer.parseInt(sb.toString()));
				oper.add(String.valueOf(line.charAt(i)));
				sb.setLength(0);
			}
		}
		int answer = numb.get(0);
		
		for (int i = 0; i < oper.size(); i++) {
			if (check == false) {
				if (oper.get(i).equals("-")) {
					tmp += numb.get(i + 1);
					check = true;
				} else {
					answer += numb.get(i + 1);
				}
				if (i == oper.size() - 1) {
					answer -= tmp;
				}
			} else {
				if (oper.get(i).equals("-")) {
					answer -= tmp;
					tmp = 0;
					tmp += numb.get(i + 1);
					if (i == oper.size() - 1) {
						answer -= numb.get(i + 1);
					}
				} else {
					tmp += numb.get(i + 1);
					if (i == oper.size() - 1) {
						answer -= tmp;
					}
				}			
			}
		}
		System.out.println(answer);
	}
}
