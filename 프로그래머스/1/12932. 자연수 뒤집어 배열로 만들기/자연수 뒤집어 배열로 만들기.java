import java.util.*;
class Solution {
    public int[] solution(long n) {
        String[] numbers = String.valueOf(n).split("");
        
        int[] answer = new int[numbers.length];
        
        for(int i = 0; i < numbers.length; i++){
            answer[i] = Integer.parseInt(numbers[numbers.length -1 - i]);
        }
        
        return answer;
    }
}