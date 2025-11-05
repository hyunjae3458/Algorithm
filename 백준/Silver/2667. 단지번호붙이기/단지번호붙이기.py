from collections import deque

N = int(input())
grid = [
    list(map(int,input()))
    for _ in range(N)
]

is_apt = [
    [False] * N
    for _ in range(N)
]

apt_lst = []

def init_apt():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                is_apt[i][j] = True

def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < N

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    is_apt[x][y] = False

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]
    
    while q:
        apt_x,apt_y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = apt_x + dx, apt_y + dy
            if in_range(nx,ny) and grid[nx][ny] and is_apt[nx][ny] == True:
                q.append((nx,ny))
                is_apt[nx][ny] = False
                cnt += 1
    return cnt

init_apt()

for i in range(N):
    for j in range(N):
        if is_apt[i][j] == True:
            apt_lst.append(bfs(i,j))

apt_lst.sort()
print(len(apt_lst))
for apt_num in apt_lst:
    print(apt_num)