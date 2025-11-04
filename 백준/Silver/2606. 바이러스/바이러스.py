from collections import deque
computer = int(input())
n = int(input())
combine = [list(map(int,input().split())) for _ in range(n)]

graph = [ [] for _ in range(computer + 1)]

for a,b in combine:
    graph[a].append(b)
    graph[b].append(a)

infect = [False] * (computer + 1)
infect[1] = True

cnt = 0
def bfs(graph,infect,start):
    global cnt
    q = deque()
    q.append(start)

    while q:
        com = q.popleft()
        for i in graph[com]:
            if infect[i] == False:
                infect[i] = True
                cnt += 1
                q.append(i)

bfs(graph,infect,1)
print(cnt)

                