N = int(input())
num = 0
a = 0

# 반복
while(1):
    # a가 N에 도달하면 탈출하면서 num 출력
    if a == N:
        print(num)
        break
    # num 하나씩 추가하며
    num += 1
    # num이 666을 포함하면 a + 1 
    if ("666" in str(num)):
        a += 1
