import sys
input = sys.stdin.readline

n = int(input())
arr = []
# 합을 담을 리스트 생성
dp = [
    [0 for _ in range(n)] for _ in range(n)
]

# 입력받을 리스트
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 합을 담을 리스트 0,0를 초기화
dp[0][0] = arr[0][0]
# 현 좌표에서 아래칸 , 으론쪽 대각선 칸으로 값을 더해보고 더 큰값을 dp에 저장
for i in range(len(arr)-1):
    for j in range(len(arr[i])):
        if (dp[i][j] + arr[i+1][j]) > dp[i+1][j]: 
            dp[i+1][j] = dp[i][j] + arr[i+1][j]

        if (dp[i][j] + arr[i+1][j+1]) > dp[i+1][j+1]:
            dp[i+1][j+1] = dp[i][j] + arr[i+1][j+1]    

# 마지막 줄이 최종합이므로 마지막 y축의 리스트 요소들중 가장 큰값을 출력
print(max(dp[n-1]))