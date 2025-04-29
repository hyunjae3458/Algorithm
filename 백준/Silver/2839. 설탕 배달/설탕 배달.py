# 5로 나누어질때
# 최소한의 3과 최대한의 5로 이루어질때
# 3으로 나누어질때
# 나누어지지 않을때

N = int(input())  

sol = 0

if N % 5 == 0:
    print(N //5)
else:
    while N > 0:
        sol += 1
        N -= 3
        if N % 5 == 0:
            sol += N //5
            print(sol)
            break
        elif N == 1 or N == 2:
            print(-1)
        elif N == 0:
            print(sol)



