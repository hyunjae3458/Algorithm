

def solution(players, m, k):
    dp = [0 for _ in range(len(players))]
    count = 0
    for i in range(len(players)):
        if players[i] >= m:
            if players[i] // m >= dp[i]:
                add_suv = (players[i] // m - dp[i])
                for j in range(min(k,len(dp)-i)): 
                    dp[i + j] += add_suv
                count += add_suv
        
        
    return count