from collections import deque
import sys
input = sys.stdin.readline
MIN_SIZE = sys.maxsize

N,K = map(int,input().split())

pos = [MIN_SIZE] * 100001

def in_range(nx):
    return nx >=0 and nx < 100001

def bfs(x):
    q = deque() 
    q.append(x)
    pos[x] = 0
    
    while q:
        cur_x = q.popleft()
        if cur_x == K:
            return pos[cur_x]
        for nx in (2*cur_x , cur_x - 1, cur_x + 1):
            if in_range(nx) and pos[nx] == MIN_SIZE:
                if nx == 2*cur_x:
                    pos[nx] = pos[cur_x]
                else:
                    pos[nx] = pos[cur_x] + 1
                q.append(nx)
                
    return 0
print(bfs(N))
         

