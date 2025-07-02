import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
answer = deque()

for _ in range(N):
    command = input().split()
    if command[0] == "push_front":
        answer.appendleft(command[1])
    if command[0] == "push_back":
        answer.append(command[1])
    if command[0] == "pop_front":
        if not answer:
            print(-1)
        else:
            print(answer.popleft())
    if command[0] == "pop_back":
        if not answer:
            print(-1)
        else:
            print(answer.pop())
    if command[0] == "size":
        print(len(answer))
    if command[0] == "empty":
        if not answer:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if not answer:
            print(-1)
        else:
            print(answer[0])        
    if command[0] == "back":
        if not answer:
            print(-1)
        else:
            print(answer[-1])   