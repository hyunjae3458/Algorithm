# 아이디어: 인덱스를 스택에 저장하고 해당 인덱스 값의 오른쪽 값과 비교하며 조건에 만족할 시 해당 인덱스 pop해서 해당 값을 ans로 할당

T = int(input()) # 배열의 크기 입력

numbers = list(map(int,input().split()))[:T] # 입력 받은 크기만큼의 배열에 들어갈 요소들 입력

stack = [] # 인덱스를 저장할 스택
ans = [-1] * T # 우큰수를 저장할 리스트 , -1 로 초기화함
 
for i in range(T): # 인덱스 0~3까지 
    while stack and numbers[stack[-1]] < numbers[i]: # stack의 내용이이 있으면서 인덱스가 i인 요소가 스택의 최상단 값을을 인덱스로한 요소보다 크면 계속 반복
        idx = stack.pop() # 스택의 최상단 pop해서 idx 변수에 저장
        ans[idx] = numbers[i] # ans 리스트의 idx번째 요소를 number 리스트의 i번째 요소로 할당당
    stack.append(i) # 스택이 없거나 인덱스가 i인 요소가 스택의 최상단 값을을 인덱스로한 요소보다 작으면 i를 스택에 추가

print(*ans)