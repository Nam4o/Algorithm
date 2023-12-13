import java.io.*;
import java.util.*;

class Solution {
    
    static int len;

    
    public boolean solution(String[] phone_book) {

        boolean answer = true;
        
    
        Arrays.sort(phone_book, (o1, o2) -> o1.length() - o2.length());
        
        HashSet<String> set = new HashSet();
        
        set.add(phone_book[0]);
        
        for (int i = 1; i < phone_book.length; i++) {
            for (int j = phone_book[0].length(); j <= phone_book[i].length(); j++) {
                String inner = phone_book[i].substring(0, j);
                if (set.contains(inner)) {
                    answer = false;
                    return answer;
                }
            }
            set.add(phone_book[i]);
        }
        
        
        
        return answer;
    }
}