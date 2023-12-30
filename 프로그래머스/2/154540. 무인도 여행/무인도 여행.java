import java.util.*;
import java.io.*;

class Solution {
    static int x, y;
    static int[] start = new int[2];
    
    static int[] di = {0, 1, 0, -1}, dj = {1, 0, -1, 0};
    static boolean[][] visited;
    public ArrayList solution(String[] maps) throws IOException {
        // int[] answer = {};
        ArrayList<Integer> answer = new ArrayList();
        
        x = maps.length;
        y = maps[0].length();
        
        visited = new boolean[x][y];
        
        // bfs();
        // System.out.println(maps[0].charAt(0));
        int len;
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (visited[i][j] == false && maps[i].charAt(j) != 'X') {
                    start[0] = i;
                    start[1] = j;
                    answer.add(bfs(start, maps));
                    // System.out.println(bfs(start, maps));
                    
                    // System.out.println(maps[i].charAt(j)- '0' + 1 );
                }
            }
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        } else {
            Collections.sort(answer);
        }
        
        return answer;
        
    }
    
    
    public int bfs(int[] start, String[] maps) {
        ArrayDeque<int[]> deq = new ArrayDeque();
        deq.add(start);
        visited[start[0]][start[1]] = true;
        
        int cnt = maps[start[0]].charAt(start[1]) - '0';
        
        while (!deq.isEmpty()) {
            int[] now = deq.pollFirst();
            for (int k = 0; k < 4; k++) {
                int nowX = now[0] + di[k], nowY = now[1] + dj[k];
                if (nowX >= 0 && nowX < x && nowY >= 0 && nowY < y && visited[nowX][nowY] == false && maps[nowX].charAt(nowY) != 'X') {
                    int[] tmp = {nowX, nowY};
                    deq.add(tmp);
                    visited[nowX][nowY] = true;
                    cnt += maps[nowX].charAt(nowY) - '0';
                }
            }
            
        }
        return cnt;
    }
}