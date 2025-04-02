def sol(N):
    # 문자를 담을 문자열 
    output = ""

    # T를 기점으로 규칙을 변경함
    T = (2*N-1) // 2

    for i in range(0,T + 1): # 줄 갯수 (0~4)
        for j in range(i,T): # 공백 넣기
            output += " " 
        for n in range(0,2*i+1): # 별 넣기
            output += "*"
        output += "\n" # 줄바꿈
    for i in range(1, T + 1): # 줄갯수 (규칙 변경 5~8)
        for j in range(0,i): # 공백 넣기
            output += " "
        for n in range(2*i - 1,2*T): # 별 넣기
            output += "*"
        output += "\n" 
    return output # 문자열 리턴


N = int(input())
print(sol(N))
