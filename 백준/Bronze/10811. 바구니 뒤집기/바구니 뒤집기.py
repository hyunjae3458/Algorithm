N , M = map(int, input().split()) # 바구니 갯수와 몇번 역순으로 할건지 입력받음
num_list = [] # 바구니를 담을 리스트 생성

for i in range(1,N+1):  # 입력받은 바구니 개수 만큼 리스트에 넣기
    num_list.append(i)

for _ in range(M): # 입력 받은 역순 개수 동안
    i,j = map(int,input().split()) # 역순할 범위를 입력 받음
    while(i < j):  # 범위를 좁혀가며 역순으로 바꿈
        num_list[i-1],num_list[j-1] = num_list[j-1], num_list[i-1] 
        i += 1
        j -= 1
    
print(*num_list) # 리스트 요소들을 출력