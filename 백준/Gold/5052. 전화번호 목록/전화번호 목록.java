import java.io.*;
import java.util.*;

public class Main {
	static int t, n;
	static String[] arr;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		t = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for(int tc = 0; tc < t; tc++) {
			n = Integer.parseInt(br.readLine());
			arr = new String[n];
			for(int i = 0; i < n; i++) {
				arr[i] = br.readLine();
			}
			if (solution(arr) == false) {
				sb.append("NO" + "\n");
			} else {
				sb.append("YES" + "\n");
			}
			
		}
		System.out.println(sb);
	}
    static boolean solution(String[] phone_book) {
        Arrays.sort(phone_book, (o1, o2)->{
            return o1.length()-o2.length();
        });
        boolean answer = true;
        HashSet<String> hs = new HashSet<>();
        hs.add(phone_book[0]);
        for(int i = 1; i < phone_book.length; i++){
            for(int j = phone_book[0].length(); j <= phone_book[i].length(); j++){
                String now = phone_book[i].substring(0, j);
                if(hs.contains(now)) {
                    answer = false;
                    return answer;
                }
            }
            hs.add(phone_book[i]);
        }
        return answer;
    }
		
	

}
