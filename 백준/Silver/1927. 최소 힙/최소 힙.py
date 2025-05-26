import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
            continue
        heap_out = heapq.heappop(heap)
        print(heap_out)
    else:
        heapq.heappush(heap,x)