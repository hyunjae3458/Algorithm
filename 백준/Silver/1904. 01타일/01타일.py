import sys
input = sys.stdin.readline

N = int(input())

# N = 1,2 초기화
arr = [0,1,2]


# 다음 N에는 전, 전전 N의 합
for i in range(3,N+1):
    arr.append((arr[i-1] + arr[i-2]) % 15746)

print(arr[N])