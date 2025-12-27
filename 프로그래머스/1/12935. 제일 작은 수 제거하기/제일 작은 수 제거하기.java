import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> lst = new ArrayList<>();
        int answer = 0;
        for(int num : arr){
            lst.add(num);
        }
        
        lst.removeIf(n -> n == Collections.min(lst));
        int[] arr2;
        
        if(lst.isEmpty()){
            arr2 = new int[1];
            arr2[0] = -1;
            return arr2;
        }
        
        arr2 = new int[lst.size()];
        for(int i = 0; i < lst.size(); i++){
            arr2[i] = lst.get(i);
        }
        
        return arr2;
    }
}