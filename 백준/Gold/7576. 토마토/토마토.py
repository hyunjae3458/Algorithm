from collections import deque
import sys
input = sys.stdin.readline

M,N = map(int,input().split())

tomato_box = [
    list(map(int,input().split()))
    for _ in range(N)
]

dp = [
    [0] * M
    for _ in range(N)
]

q = deque()

def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < M

def bfs():

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    while q:
        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx ,ny = cur_x + dx , cur_y + dy
            if in_range(nx,ny):
                if tomato_box[nx][ny] == 0:
                    tomato_box[nx][ny] = 1
                    dp[nx][ny] = dp[cur_x][cur_y] + 1
                    q.append((nx,ny))

# 이미 토마토가 자란 좌표를 모두 q에 넣음
all_grown = True
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            q.append((i,j))
            dp[i][j] = 1
        if tomato_box[i][j] == -1:
            dp[i][j] = -1
        if tomato_box[i][j] == 0:
            all_grown = False

bfs()

# 모두 자랐을때 날짜를 구함

max_day = 0
for i in range(N):
    for j in range(M):
        max_day = max(max_day, dp[i][j])
        # 안자란 좌표가 있으면 -1출력 후 종료
        if dp[i][j] == 0:
            print(-1)
            exit(0)

if all_grown:
    print(0)
else:
    print(max_day - 1)

        
