import sys
input = sys.stdin.readline

N = int(input())
arr = []
sol = 1

# 리시트로 시작 시간과 끝 시간을 묶어서 담음 
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 끝나는 시간이 빠를수록 앞으로 가도록, 끝나는 시간이 같다면 시작시간이 먼저인것이 앞으로 가도록
arr.sort(key=lambda x: (x[1], x[0]))

# 끝 시간을 저장해두고
end_point = arr[0][1]
for i in range(1,len(arr)):
    if arr[i][0] >= end_point: # 끝 시간보다 같거나 큰 시간이 시작 시간으로 오는 요소가 있다면
        sol += 1 # 가능 회의 시간대 추가 
        end_point = arr[i][1] # 해당 요소의 끝나는 시간을 새로운 끝시간으로 저장


print(sol)
    


