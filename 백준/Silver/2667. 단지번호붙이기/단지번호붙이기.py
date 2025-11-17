from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

grid = [
    list(map(int,input().strip()))
    for _ in range(N)
]

dp = [
    [0] * N
    for _ in range(N)
]

visited = [
    [False] * N
    for _ in range(N)
]


def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < N

apt = []
 
def bfs(x,y,apt_num):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dp[x][y] = 1
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    while q:
        cur_x,cur_y = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                if dp[nx][ny] == 0:
                    dp[nx][ny] = 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    apt_num += 1
    return apt_num
    
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            apt.append(bfs(i,j,1))

apt.sort()
print(len(apt))
for i in apt:
    print(i)


