from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
grid = [
    [0] * N
    for _ in range(N)
]

# 시작 지점 초기화
grid[0][0] = 1

K = int(input())

for _ in range(K):
    x,y = map(int,input().split())
    # 좌표위 2는 사과의 위치
    grid[x-1][y-1] = 2

L = int(input())

seconds = []
directions = []
for _ in range(L):
    sec, dir = input().split()
    seconds.append(int(sec))
    directions.append(dir)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(nx,ny):
    return nx >= 0 and nx < N and ny >= 0 and ny < N
    

head_x,head_y,cur_dir = 0,0,0
time = 0

pos = deque([(0,0)])
while True:
    time += 1
    head_x,head_y  = head_x + dxs[cur_dir], head_y + dys[cur_dir]
    pos.append((head_x,head_y))
    if not in_range(head_x,head_y) or grid[head_x][head_y] == 1:
        print(time)
        exit(0)
    if grid[head_x][head_y] != 2:
        tail_x,tail_y = pos.popleft()
        grid[tail_x][tail_y] = 0
    grid[head_x][head_y] = 1
    if time in seconds:
        if directions[seconds.index(time)] == "L":
            cur_dir = (cur_dir % 4 or 4) - 1
        else:
            cur_dir = (cur_dir + 1) % 4
    

        

