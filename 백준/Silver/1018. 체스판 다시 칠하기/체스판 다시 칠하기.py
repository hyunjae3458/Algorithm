import sys
input = sys.stdin.readline

N,M = map(int, input().split())
cnt = [] # 시작점마다 다시 칠한 수를 저장할 리스트트
grid = [
    input()
    for _ in range(N)
]

# 8x8을 가질 수 있도록 -7을 해준다 (시작점 기준 구하기)
for a in range(N-7):
    for b in range(M-7):
        w_index = 0 # 시작점이 W일때 다시 칠해야할 수
        b_index = 0 # 시작점이 B일때 다시 칠해야할 수
        # 시작(a,b)
        for i in range(a,a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 짝수칸
                    # 시작점이 W로 칠해졌을때 짝수칸 중에 W가 아닌 칸들
                    if grid[i][j] != "W": 
                        w_index += 1 
                    # 시작점이 B로 칠해졌을때 짝수칸 중에 B가 아닌 칸들
                    else: 
                        b_index += 1 
                else: # 홀수 칸 
                    # 시작점이 W로 칠해졌을때 홀수칸 중에  B가 아닌 칸들
                    if grid[i][j] != "B":
                        w_index += 1 
                    # 시작점이 B로 칠해졌을때 홀수칸 중에 W가 아닌 칸들들
                    else:
                        b_index += 1 
        # 새로운 시작점으로 가기전 다시 칠한 수를 저장
        cnt.append(w_index)
        cnt.append(b_index)                 

print(min(cnt))