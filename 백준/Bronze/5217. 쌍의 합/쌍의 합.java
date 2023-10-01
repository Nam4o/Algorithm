import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int tc = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < tc; i++) {
			int n = Integer.parseInt(br.readLine());
			
			writer.write("Pairs for " + n + ":");
			
			ArrayList<Object> pair = new ArrayList<>();
			
			for (int j = 1; j < n - 1; j ++) {
				for (int k = j + 1; k < n; k ++) {
					if (j + k == n) {
						String tmp = "";
						tmp += Integer.toString(j);
						tmp += " ";
						tmp += Integer.toString(k);
						pair.add(tmp);						
					}
				}
			}
			for (int w = 0; w < pair.size(); w++) {
				writer.write(" " + pair.get(w));
				if (w != pair.size() - 1) {
					writer.write(",");
				}
			}
			writer.write("\n");
		}
	writer.flush();	
	}
}
