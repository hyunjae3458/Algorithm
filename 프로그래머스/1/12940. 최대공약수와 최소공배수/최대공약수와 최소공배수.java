import java.lang.Math;
class Solution {
    public int getAns(int a, int b){
        while(b != 0){
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int max = Math.max(n,m);
        int min = Math.min(n,m);
        
        answer[0] = getAns(max,min);
        answer[1] = max * min / answer[0];
        
        return answer;
    }
}