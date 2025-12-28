import java.util.*;
class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        
        for(char ch : arr){
            sb.append(ch);
        }
        
        return sb.reverse().toString();
    }
}