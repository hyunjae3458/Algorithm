import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0] * (N+1) # 진입차수 개수
graph = [[] for _ in range(N+1)] # 해당 노드의 간선의 점

# 진입차수 리스트와 그래프 체음
for _ in range(M):
    a,b = map(int, input().split())
    # a가 b의 선행이기 때문에 b진입차수 +1, a는 b에 연결
    graph[a].append(b)
    indegree[b] += 1 

# 답을 담을 리스트, 노드를 담을 큐
result = []
queue = deque()

#큐에 진입차수가 0인 노드를 담음
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

# 큐가 빌때까지지
while(queue):
    node = queue.popleft() # 큐에 왼쪽부터 빼서
    result.append(node) # 답에 담음
    for i in graph[node]: # 해당 노드를 답에 담으면
        indegree[i] -= 1 # 해당 간선의 점의 진입차수를 -1 
        if indegree[i] == 0: # 만약  해당 간선의 점도 진입차수가 0이 되면 큐에 담음
            queue.append(i)

print(*result)

