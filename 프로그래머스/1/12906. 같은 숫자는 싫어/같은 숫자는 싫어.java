import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> st = new Stack<>();
        for(int i = 0; i < arr.length; i++){
            if(st.empty()){
                st.push(arr[i]);
            }
            else{
                if(arr[i] == st.peek()){
                    continue;
                }
                else{
                    st.push(arr[i]);
                }    
            }
        }
        
        int[] answer = new int[st.size()];
        for(int i= 0; i < st.size(); i++){
            answer[i] = st.get(i);
        }

        return answer;
    }
}