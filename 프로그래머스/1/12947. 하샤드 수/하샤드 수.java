import java.util.*;
class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        StringBuilder sb = new StringBuilder();
        String[] numbers = String.valueOf(x).split("");
        int sum = 0;
        for(String number : numbers){
            sum += Integer.parseInt(number);
        }
        
        if(x % sum != 0){
            answer = false; 
        }
        
        return answer;
    }
}