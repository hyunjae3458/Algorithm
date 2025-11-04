from collections import deque
N,M = map(int, input().split())

grid = [list(map(int,input())) for _ in range(N)]


def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < M


def bfs(x,y):
    q = deque()
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx,ny))

    return grid[N-1][M-1]

print(bfs(0,0))