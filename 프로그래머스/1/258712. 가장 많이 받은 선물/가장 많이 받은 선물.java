import java.util.*;

class Solution {
//     내 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로
//     다음 달에 누가 선물을 많이 받을지 예측
//     조건1. 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에
//          더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다.
//     조건2. 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면,
//          선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음
//          *선물지수 : 이번 달까지 내가 친구들에게 준 선물의 수 - 받은 선물의 수
//     조건3. 두 사람의 선물 지수도 같다면 다음 달에 선물 주고받기 x
    
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int friendsSize = friends.length;
        Map<String, List<String>> history = new HashMap<>();
        
//      {0(번친구): 1, 1(번친구): 2 }
        Map<Integer, Integer> giftPoint = new HashMap<>();
//      {"muzi" : 0(번), "frodo": 1(번)}
        Map<String, Integer> friendsInfo = new HashMap<>();
        
        
        int[][] tmp = new int[friendsSize][friendsSize];
        for(int i = 0; i < friendsSize; i++) {
            friendsInfo.put(friends[i], i);
            giftPoint.put(i, 0);
        }
        
//         for(String friend : friends) {
//             giftPoint.put(friendsInfo.get(friend), 0);
//         }
        
        
        
//         gift 리스트를 순회하면서 선물 주고받은 내역을 history에 저장
        for(String gift : gifts) {
            String[] container = gift.split(" ");
            String giver = container[0];
            String taker = container[1];
            int tmp1 = friendsInfo.get(giver);
            int tmp2 = friendsInfo.get(taker);
            giftPoint.put(friendsInfo.get(giver), giftPoint.get(tmp1) + 1);
            giftPoint.put(friendsInfo.get(taker), giftPoint.get(tmp2) - 1);
            tmp[friendsInfo.get(giver)][friendsInfo.get(taker)] += 1;
            // System.out.println("디버깅");
            // System.out.println(tmp[friendsInfo.get(giver)][friendsInfo.get(taker)]);
        }
        
        for(int k = 0; k < friendsSize; k++) {
            int count = 0;
            for(int j = 0; j < friendsSize; j++) {
                if(k == j) {
                    continue;
                } else {
                    if(tmp[k][j] > tmp[j][k]) {
                        count += 1;
                    } 
                    else if ((tmp[k][j] == 0 && tmp[j][k] == 0) || (tmp[k][j] == tmp[j][k])) {
                        if(giftPoint.get(k) > giftPoint.get(j)) {
                            count += 1;
                        }
                    } 
                }
            }
            if (count >= answer) {
                answer = count;
            }
        }
        return answer;
    }
}