import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
myQueue = deque([])
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        myQueue.append(command[1])
    if command[0] == "pop":
        if not myQueue:
            print(-1)
        else:
            print(myQueue.popleft())
    if command[0] == "size":
        print(len(myQueue))
    if command[0] == "empty":
        if not myQueue:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if not myQueue:
            print(-1)
        else:
            print(myQueue[0])
    if command[0] == "back":
        if not myQueue:
            print(-1)
        else:
            print(myQueue[len(myQueue) - 1])
        