class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int sumNum = 0;
        for(int i = 0; i < absolutes.length; i++){
            sumNum += absolutes[i] * (signs[i]? 1 : -1);
        }
        
        
        return sumNum;
    }
}