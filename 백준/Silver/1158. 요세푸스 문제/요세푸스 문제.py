import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
circle = deque()
answer = []

for i in range(1,N+1):
    circle.append(i)

# 큐 안에 요소가 없을때까지
while(circle):
    # 제거하려는 인덱스 앞까지 뒤로 보낸뒤
    for _ in range(K-1):
        circle.append(circle.popleft())
    # 큐의 가장 앞 요소를 정답 리스트에 추가
    answer.append(circle.popleft())
    
print("<" + ", ".join(map(str,answer)) + ">")