N = int(input())

def fec(n):
    if n > 1:
        return n * fec(n-1)
    else:
        return 1

if N == 0:
    print(1)
else:
    print(fec(N))