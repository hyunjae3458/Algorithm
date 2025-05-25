import sys
input = sys.stdin.readline

# 색종이 개수
N = int(input())
arr = [
    [0] * 100
    for _ in range(101)
]
cnt = 0

for _ in range(N):
    a,b = map(int, input().split())
    for i in range(b-1,b+9):
        for j in range(a-1,a+9):
            if arr[i][j] == 1:
                continue
            else:
                arr[i][j] = 1


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
           
