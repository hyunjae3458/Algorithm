import java.util.*;
class Solution {
    // 유저의 경우의 수를 담을 리스트
    private List<List<String>> userLst = new ArrayList<>();
    // 경우의 수를 걸러낼 셋
    private Set<Set<String>> answerSet = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        for(String str : banned_id){
            int strSize = str.length();
            // 해당 벤 아이디가 될 수 있는 아이디를 담을 리스트
            List<String> lst = new ArrayList<>();
            
            for(String user : user_id){
                if(strSize == user.length()){
                    if(check(str,user)) {
                        lst.add(user);
                    }
                }  
            }
            userLst.add(lst);
        }
        
        // 아이디들로 경우의 수 구하기
        Set<String> banned = new HashSet<>();
        count(0,banned);
        System.out.println(answerSet);
        return answerSet.size();
    }
    
    private boolean check(String ban, String user){
        for(int i = 0; i < ban.length(); i++){
            if(ban.charAt(i) == '*' || ban.charAt(i) == user.charAt(i)) continue;
            else return false;
        }
        return true;
    }
    
    private void count(int cnt, Set<String> banned){
        if(cnt == userLst.size()){
            answerSet.add(new HashSet<>(banned));
            return;
        }
        
        for(String s : userLst.get(cnt)){
            if(banned.contains(s)) continue;
            banned.add(s);
            count(cnt + 1, banned);
            banned.remove(s);
        }
    }
}