import sys
input = sys.stdin.readline

N = int(input())

# 춤추는 사람을 모을 집합(중복으로 들어가지지 않음)
dance = set()

for _ in range(N):
    a,b = input().split()
    # 총총이 있으면 집합에 둘다 추가
    if a == "ChongChong" or b == "ChongChong":
        dance.add(a)
        dance.add(b)
    # 만약 두 이름중 하나라도 춤추는 사람에 포함되어 있으면 둘 다 추가 (집합이라 중복으로 추가 안되므로 춤추지 않는 사람만 추가됨)
    elif a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
 
