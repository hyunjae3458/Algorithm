import sys
input = sys.stdin.readline

N = int(input())

work = [[0,0]]
for _ in range(N):
    work.append(list(map(int,input().split())))

dp = [0] * (N+1)


for i in range(1,N+1):
    dp[i] = max(dp[i-1],dp[i])
    if i+work[i][0] <= N+1:
        dp[i+work[i][0]-1] = max(dp[i+work[i][0]-1], dp[i-1] + work[i][1])
        
print(max(dp))