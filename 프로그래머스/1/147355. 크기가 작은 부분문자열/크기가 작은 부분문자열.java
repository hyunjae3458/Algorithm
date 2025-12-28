import java.util.*;
class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long pValue = Long.parseLong(p);
        for(int i = 0; i <= t.length() - p.length(); i++){
            String str = t.substring(i,i+p.length());
            if( pValue>= Long.parseLong(str)){
                answer += 1;
            }
        }
        
        return answer;
    }
}