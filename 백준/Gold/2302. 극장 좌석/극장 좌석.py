N = int(input())
M = int(input())
vip_seat = [
    int(input())
    for _ in range(M)
]

dp = [0] * (N+1)

dp[0],dp[1] = 1,1

for i in range(2,N+1):
    dp[i] = dp[i-2] + dp[i-1]

num_lst = []
num = 0
for i in range(1,N+1):
    if i in vip_seat:
        num_lst.append(num)
        num = 0
        continue
    num += 1
num_lst.append(num)

answer = 1
for seg in num_lst:
    answer *= dp[seg]


print(answer)
