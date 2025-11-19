from collections import deque

R,C,T = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(R)
]

def in_range(nx,ny):
    return nx >= 0 and nx < R and ny >= 0 and ny < C

def spread():
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]
    while q:
        cur_x,cur_y,dust = q.popleft()
        spread_cnt = 0
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and grid[nx][ny] > -1:
                grid[nx][ny] += dust // 5
                spread_cnt += 1
        grid[cur_x][cur_y] -= (dust//5) * spread_cnt

def air_cleaner_time(x):
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]

    temp = 0
    dir = 0
    cur_x,cur_y = x,0
    while True:
        nx,ny = cur_x + dxs[dir], cur_y + dys[dir]
        if nx == R or ny == C or ny == -1:
            dir = (dir +1) % 4
            continue
        if nx == x and ny == 0:
            break
        grid[nx][ny] , temp = temp , grid[nx][ny]
        cur_x,cur_y = nx,ny

def air_cleaner_anti_time(x):
    dxs = [0,-1,0,1]
    dys = [1,0,-1,0]

    temp = 0
    dir = 0
    cur_x,cur_y = x,0
    while True:
        nx,ny = cur_x + dxs[dir], cur_y + dys[dir]
        if nx == -1 or ny == C or ny == -1:
            dir = (dir +1) % 4
            continue
        if nx == x and ny == 0:
            break
        grid[nx][ny] , temp = temp , grid[nx][ny]
        cur_x,cur_y = nx,ny

air_cleaner_x = []
q = deque()
for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                q.append((i,j,grid[i][j]))
            if grid[i][j] == -1:
                air_cleaner_x.append(i)
for _ in range(T):
    spread()
    air_cleaner_anti_time(air_cleaner_x[0])
    air_cleaner_time(air_cleaner_x[1])
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                q.append((i,j,grid[i][j]))

sum_dust = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] > 0:
            sum_dust += grid[i][j]

print(sum_dust)