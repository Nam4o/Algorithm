import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String text = br.readLine();
		
		ArrayList<String> arr = new ArrayList<>();
		for (int i = 0; i < text.length(); i ++) {
			String tmp = text.substring(i);
			arr.add(tmp);
				
		}
		arr.sort(null);
		for (int j = 0; j < arr.size(); j++) {
			writer.write(arr.get(j) + "\n");
		}
	writer.flush();
	writer.close();
	}

}
