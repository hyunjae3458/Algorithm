N = int(input())
MIN = int(10**6)
# 빨, 초, 파
rgb_price = [
    list(map(int,input().split()))
    for _ in range(N)
]

# 현재 칠할 집은 전에 선택한 집을 칠한 최솟값에 현재 칠할 최소값을 더한것

# 빨 , 초 , 파
dp = [
    [0] * 3
    for _ in range(N)
]

# 처음 칠할 집 초기화
for i in range(3):
    dp[0][i] = rgb_price[0][i]

for i in range(1,N):
    # 빨
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb_price[i][0]
    # 초
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb_price[i][1]
    # 파
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb_price[i][2]


print(min(dp[N-1]))

