import java.util.ArrayDeque;

class Solution {

    static int numberOfArea = 0;
    static int maxSizeOfOneArea = 0;
    static int check, M, N;
    static int[] answer = new int[2];
    static int[][] visited, board;
    static int[] di = {0, 1, 0, -1}, dj = {1, 0, -1, 0};

    public int[] solution(int m, int n, int[][] picture) {
        M = m;
        N = n;
        visited = new int[M][N];
        board = new int[M][N];

        // 수정된 부분: 초기화를 위해 각 변수를 0으로 설정
        numberOfArea = 0;
        maxSizeOfOneArea = 0;

        for (int x = 0; x < M; x++) {
            for (int y = 0; y < N; y++) {
                board[x][y] = picture[x][y];
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++){
                if (visited[i][j] == 0 && board[i][j] != 0) {
                    // 수정된 부분: bfs 메서드 호출 시 시작 지점을 전달
                    int[] start = {i, j};
                    check = bfs(board[i][j], start);

                    numberOfArea += 1;

                    if (check > maxSizeOfOneArea) {
                        maxSizeOfOneArea = check;
                    }
                }
            }
        }

        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    // 수정된 bfs 메서드
    public int bfs(int num, int[] start) {
        ArrayDeque<int[]> deq = new ArrayDeque<>();
        deq.add(start);
        visited[start[0]][start[1]] = 1;

        int wid = 1;

        while (!deq.isEmpty()) {
            int[] now = deq.pollFirst();
            for (int k = 0; k < 4; k++) {
                int ni = now[0] + di[k], nj = now[1] + dj[k];
                if (ni >= 0 && ni < M && nj >= 0 && nj < N && visited[ni][nj] == 0 && board[ni][nj] == num) {
                    wid += 1;
                    int[] tmp = {ni, nj};
                    deq.add(tmp);
                    visited[ni][nj] = 1;
                }
            }
        }

        return wid;
    }
}
