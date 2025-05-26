import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            result = (heapq.heappop(heap))*-1
            print(result)
    else:              
        heapq.heappush(heap,-x)
            