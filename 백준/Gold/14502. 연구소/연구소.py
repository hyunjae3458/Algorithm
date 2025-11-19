# 조합으로 벽 세우는 경우의 수 구함
# 세우는 경우의수 중 안전 지역이 가장 많은 것
from collections import deque
from itertools import combinations

N,M = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(N)
]
dp = [
    [0] * M
    for _ in range(N)
]

walls = []
q = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            walls.append((i,j))


wall_pos_lst = list(combinations(walls,3))

def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < M

def get_virus():
    q = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                q.append((i,j))
    return q

def bfs():
    q = get_virus()
    dxs = [1,0,-1,0]
    dys = [0,-1,0,1]
    
    while q:
        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx,ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and dp[nx][ny] == 0:
                dp[nx][ny] = 2
                q.append((nx,ny))
    

def new_grid():
    for i in range(N):
        for j in range(M):
            dp[i][j] = grid[i][j]

def get_safe():
    safe_cnt = 0
    for i in range(N):
        for j in range(M):
            if dp[i][j] == 0:
                safe_cnt += 1
    return safe_cnt
max_safe = -1
for wall_pos in wall_pos_lst:
    new_grid()
    for x,y in wall_pos:
        dp[x][y] = 1
    bfs()
    max_safe = max(max_safe,get_safe())

print(max_safe)

