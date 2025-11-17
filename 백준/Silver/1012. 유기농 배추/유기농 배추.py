from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # M = 가로 , N = 세로
    M,N,K = map(int,input().split())
    cabbage = [
        [0] * M
        for _ in range(N)
    ]

    for _ in range(K):
        y,x = map(int,input().split())
        cabbage[x][y] = 1

    cabbage_exisit = [
        [False] * M
        for _ in range(N)
    ]

    def in_range(nx,ny):
        return nx >= 0 and nx < N and ny >= 0 and ny < M
    
    cnt = 0
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        cabbage_exisit[x][y] = True
        dxs = [1,0,-1,0]
        dys = [0,1,0,-1]

        while q:
            cur_x, cur_y = q.popleft()  
            
            for dx,dy in zip(dxs,dys):
                nx,ny = cur_x + dx, cur_y + dy
                if in_range(nx,ny) and cabbage[nx][ny] == 1 and not cabbage_exisit[nx][ny]:
                    cabbage_exisit[nx][ny] = True
                    q.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and cabbage_exisit[i][j] == False:
                bfs(i,j)
                cnt += 1
    
    print(cnt)
