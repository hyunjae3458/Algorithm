# b의 가장 큰값에 a의 가장 작은값
# b의 가장 작은 값에 a의 가장 큰값 
N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(N):
    answer += A[i]*B[i]

print(answer)