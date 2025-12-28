import java.util.*;
class Solution {
    public boolean solution(String s) {
        boolean answer = false;
        StringBuilder sb = new StringBuilder();
        char[] arr = s.toCharArray();
        
        int len = arr.length;
        boolean possible = true;
        
        for(char ch : arr){
            if(!Character.isDigit(ch)){
                possible = false;
            }
        }
        if((len == 4 || len == 6) && possible){
            answer = true;
        }
        
        return answer;
    }
}