# 재귀, dfs, dp 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


M, N = map(int, input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(M)
]

dp = [
    [-1] * N 
    for _ in range(M)
]

dx, dy = [1,-1,0,0] , [0,0,1,-1]

def dfs(x,y):
    # 끝 지점에 도달하면
    if x == M-1 and y == N-1:
        return 1
    
    # 만약 이미 지나간 지점이면 해당 지점의 방문횟수 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 경로 수 
    way = 0
    # 4방향으로 모두 움직여봄
    for i in range(4):
        # 이동 후 다음 지점
        nx, ny = x + dx[i], y + dy[i]
        # 만약 다음 지점이 갈 수 있는 지점이거나 이동 전 지점보다 작다면
        if 0 <= nx < M and 0 <= ny < N and grid[x][y] > grid[nx][ny]:
            # 다음 지점으로 재귀 
            way += dfs(nx,ny)
    # 이번 지점에 방문 횟수 할당
    dp[x][y] = way
    # 이번 지점 방문횟수 리턴
    return dp[x][y]

print(dfs(0,0))