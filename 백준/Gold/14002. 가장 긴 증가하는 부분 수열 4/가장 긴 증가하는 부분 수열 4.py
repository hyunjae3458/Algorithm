N = int(input())

A = list(map(int,input().split()))

dp = [1] * N
dp_lst = []

for i in A:
    dp_lst.append([i])

for i in range(1,N):
    idx = 0
    changed = False
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j] + 1)
            if dp[i] == dp[j] + 1:
                idx = j
                changed = True
    if changed:
        dp_lst[i].extend(dp_lst[idx])
        dp_lst[i].sort()

print(max(dp))
print(*(max(dp_lst,key=lambda lst : len(lst))))
