from collections import deque
import sys
input = sys.stdin.readline
N,M,V = map(int,input().split())

graph = [
    [] 
    for _ in range(N + 1)
]
visit_1= [False] * (N+1)
visit_2= [False] * (N+1)
visit_1[V],visit_2[V] = True,True

for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

dfs_answer = []
bfs_answer = []
def dfs(x):
    for next in graph[x]:
        if visit_1[next]:
            continue
        dfs_answer.append(next)
        visit_1[next] = True
        dfs(next)

    return 0

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        curr = q.popleft()
        if graph[curr]:
            for next in graph[curr]:
                if not visit_2[next]:
                    q.append(next)
                    bfs_answer.append(next)
                    visit_2[next] = True

dfs_answer.append(V)
bfs_answer.append(V)

dfs(V)
bfs(V)
print(*dfs_answer)
print(*bfs_answer)
    