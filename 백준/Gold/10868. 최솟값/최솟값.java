import java.util.*;
import java.io.*;

public class Main {
	static long tree[];
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int length = N;
		int treeH = 0;
		while(0 < length) {
			length /= 2;
			treeH++;
		}
		int treeSize = (int)Math.pow(2, treeH+1);
		tree = new long[treeSize + 1];
		int leftIndex = treeSize/2 - 1;
		
		//트리 초기화하기
		for(int i = 1; i <= treeSize; i++) {
			tree[i] = Integer.MAX_VALUE;
		}
		
		//입력값 받기
		for(int i = leftIndex+1; i <= leftIndex+N; i++) {
			tree[i] = Long.parseLong(br.readLine());
		}
		
		init(tree.length-1);
		
		StringBuilder sb = new StringBuilder();
		//명령 처리
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			s = s+leftIndex;
			e = e+leftIndex;
			sb.append(minValue(s, e)).append("\n");
		}
		System.out.println(sb);
	}
	//트리 초기화
	public static void init(int lastIndex) {
		while(0 < lastIndex) {
			tree[lastIndex/2] = Math.min(tree[lastIndex/2], tree[lastIndex]);
			lastIndex--;
		}
	}
	public static long minValue(int s, int e) {
		long Min = Integer.MAX_VALUE;
		while(s <= e) {
			if(s % 2 == 1) {
				Min = Math.min(Min, tree[s]);
				s++;
			}
			s /= 2;
			if(e % 2 == 0) {
				Min = Math.min(Min, tree[e]);
				e--;
			}
			e /= 2;
		}
		return Min;
	}
}
