N = int(input())

sol = [-1] * N # 입력받은 만큼 크기의 답을 저장할 리스트를 -1로 초기화함  
dic = {} # 각 숫자가 나온 개수를 저장할 딕션어리 
stack = [] # 인덱스를 저장할 스택

# 입력받은 크기만큼의 숫자를 저장할 리스트
output = list(map(int, input().split()))[:N]

# 리스트 내 각 숫자의 개수를 딕션어리에 저장함 
for i in output:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(N):
    # 스택에 내용이 있고 스택 최상단에 있는 인덱스의 값과 for문 인덱스의 값의 개수를 비교
    while stack and dic[output[stack[-1]]] < dic[output[i]]:
        # stack 최상단의 값을 pop해서 idx에 저장 -> 해당 idx는 오동큰수가 있다는 뜻
        idx = stack.pop()
        # 답 리스트의 해당 인덱스에 값을 할당
        sol[idx] = output[i]
    # 해당 while문을 만족 못할시 스택에 저장
    stack.append(i)
    
print(*sol)


    