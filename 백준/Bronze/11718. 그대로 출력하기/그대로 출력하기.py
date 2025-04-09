# 몇 줄 입력 받는지 안나오므로 무한 반복문을 함, 중간에 더이상 입력 받을 데이터 없을시 eof 오류가 일어나므로 try except로 탈출하기
while True: 
    try:
        output = input()
        if output == "" or len(output) > 100:
            break
        print(output.strip())
    except EOFError:
        break

