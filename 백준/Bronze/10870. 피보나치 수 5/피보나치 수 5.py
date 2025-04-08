T = int(input())



def fibonachi(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    else:
        return fibonachi(N-1) + fibonachi(N-2)
    
print(fibonachi(T))