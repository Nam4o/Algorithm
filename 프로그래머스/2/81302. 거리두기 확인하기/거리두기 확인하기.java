import java.io.*;
import java.util.*;



class Solution {
    
    
    static int[] answer, start, tmp;
    static int[][] visited;
    static int[] di = {0, 1, 0, -1}, dj = {1, 0, -1, 0};
    static String[][] place;
    static boolean check;
    
    
    public int[] solution(String[][] places) throws IOException{
        place = new String[5][5];
        place = places;
        answer = new int[5];
       
        // 전체 순회 (String[])
        for (int w = 0; w < 5; w++){
            // 한 줄 순회 (String)
            // visited 초기화
            // visited = new int[5][5];
            check = true;
            for (int i = 0; i < 5; i++) {
                // 한 줄의 한 인덱스 순회 (Char)
                for (int j = 0; j < 5; j++) {
                    
                    if (place[w][i].charAt(j) == 'P') {
                        visited = new int[5][5];
                        start = new int[2];
                        start[0] = i;
                        start[1] = j;
                        bfs(start, w);
                        if (!check) {
                            break;
                        }
                    } 
                    
                }
                if (!check) {
                            break;
                        }
            }
            if (!check) {
                answer[w] = 0;
            } else {
                answer[w] = 1;
            }
        }
        
        
        return answer;
    }
    
    static void bfs(int[] start, int idx) {
        ArrayDeque<int[]> deq = new ArrayDeque();
        deq.add(start);
        visited[start[0]][start[1]] = 1;
        
        while (!deq.isEmpty()) {
            int[] n = deq.pollFirst();
            for (int k = 0; k < 4; k++) {
                int ni = n[0] + di[k], nj = n[1] + dj[k];
                if (ni >= 0 && ni < 5 && nj >= 0 && nj < 5 && visited[ni][nj] == 0 && place[idx][ni].charAt(nj) != 'X') {
                    tmp = new int[2];
                    tmp[0] = ni;
                    tmp[1] = nj;
                    if (place[idx][ni].charAt(nj) == 'O') {
                        deq.add(tmp);
                        visited[ni][nj] = visited[n[0]][n[1]] + 1;    
                    } else {
                        if (visited[n[0]][n[1]] <= 2) {
                            check = false;
                            return;
                        } else {
                            deq.add(tmp);
                            visited[ni][nj] = visited[n[0]][n[1]] + 1;
                        }
                    }

                }
            }
        }
    }
}
