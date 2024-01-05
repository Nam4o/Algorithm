import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        // String[] spoken = new String[n];
        ArrayList<String> spoken = new ArrayList();
        
        
        int idx = 0;
        int cycle = 1;
        for (int i = 0; i < words.length; i++) {
            if (i != 0 && i % n == 0) {
                cycle ++;
            }
            if (spoken.contains(words[i])) {
                answer[0] = i % n + 1;
                answer[1] = cycle;
                break;
            }
            if (i != 0 && words[i].charAt(0) == words[i - 1].charAt(words[i - 1].length() - 1)) {
                spoken.add(words[i]);
            } else if (i != 0 && words[i].charAt(0) != words[i - 1].charAt(words[i - 1].length() - 1)) {
                answer[0] = i % n + 1;
                answer[1] = cycle;
                break;
            } else {
                spoken.add(words[i]);
            }
            
        }

        return answer;
    }
}