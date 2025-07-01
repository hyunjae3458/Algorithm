import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    PS = input()
    # 문자열을 저장할 스택 ()가 되면 pop
    check_idx = []
    
    for i in PS:
        # (가 나오면 스택에 추가
        if i == "(":
            check_idx.append(i)
        # ) 가 나오면 스택에서 ( 삭제
        if i == ")":
            # 만약 스택이 비었는데 문자열에 )가 나오면 break
            if not check_idx:
                print("NO")
                break
            check_idx.pop()
    # for 문을 끝까지 돌고 나왔을 경우 break로 for문을 탈출하면 실행 안됨
    else:
        if not check_idx:
            print("YES")
        else:
            print("NO")
    
        

            