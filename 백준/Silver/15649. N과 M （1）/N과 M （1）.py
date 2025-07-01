import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# 정답을 담을 배열
answer = []

# 백트랙
def backtrack():
    # 만약 주어진 길이의 수열이라면 해당 수열의 내용을 출력
    if len(answer) == M:
        print(*answer)
    # 배열에 들어갈 숫자를 검색
    for i in range(1,N+1):
        # 만약 그 숫자가 없다면 추가
        if i not in answer:
            answer.append(i)
            # 백트랙 재귀 -> 정답이면 출력
            backtrack()
            # 출력 완성 후 다른 경우가 있는지 부모 노드로 돌아가서 다음 i를 넣어봄
            answer.pop()

backtrack()    