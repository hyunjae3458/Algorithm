stair = int(input())

arr = [0]
for i in range(stair):
    arr.append(int(input()))

# dp -> i번째 계단을 밟았을때가 연속 j번째 밟을 경우 최대 합 
dp = [
    [0]*3 # 0: 해당 행의 계단이 연속 0번일때(안밟을때),  1: 해당 열의 계단이 연속 1번일때, 2: 해당 열의 계단이 연속 2번일때
    for _ in range(stair+1)
]

for i in range(1,stair+1):
    for j in range(3):
        # 해당 계단을 건너뛰는 경우므로 전 계단의 점수 중 높은 점수
        dp[i][0] = max(dp[i-1][1],dp[i-1][2])
        # 해당 계단은 연속 1번째이므로 전 계단의 안밟은 경우 + 점수
        dp[i][1] = dp[i-1][0] + arr[i]
        # 해당 계단은 연속 2번째이므로 전 계단의 밟은 경우 + 점수
        dp[i][2] = dp[i-1][1] + arr[i]

# 마지막 계단은 꼭 밟아야하므로 안밟은 경우 0을 제외한 둘 중 큰 수
print(max(dp[stair][1],dp[stair][2]))
