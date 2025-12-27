class Solution {
    public int solution(int[] a, int[] b) {
        int sumNum = 0;
        for(int i = 0; i < a.length; i++){
            sumNum += a[i] * b[i];
        }
        
        return sumNum;
    }
}