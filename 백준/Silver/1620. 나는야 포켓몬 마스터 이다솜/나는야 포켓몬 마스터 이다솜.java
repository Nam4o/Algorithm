import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Map<String, Object> dict1 = new HashMap<>();
		Map<Object, String> dict2 = new HashMap<>();
		
		for (int i = 1; i <= N; i++) {
			String pokemon = br.readLine();
			
			dict1.put(pokemon, i);
			dict2.put(i, pokemon);
		}
		for (int j = 0; j < M; j++) {
			String judge = br.readLine();
			
			if (Character.isDigit(judge.charAt(0)) == true) {
				int val = Integer.parseInt(judge);
				writer.write(dict2.get(val) + "\n");
			} else {
				writer.write(dict1.get(judge) + "\n");
			}
		}
		writer.flush();
	}
    
	public static <K, V> K getKey(Map<K, V> map, V value) {
		for (K key : map.keySet()) {
			if (value.equals(map.get(key))) {
				return key;
			}
		}
		return null;
	}
}
