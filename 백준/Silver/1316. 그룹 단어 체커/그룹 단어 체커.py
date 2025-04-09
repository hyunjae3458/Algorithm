import sys
N = int(input())

# 그룹단어가 아닌 문자개수 저장
cnt = 0 
out_put = []


for _ in range(N):
    out_put.append(input())

# ord() -> 아스키 번호 표현
for s in out_put:
    flag = [0] * 26 # 알파벳이 이미 한번 나왔는지 확인하기 위한 배열
    for i in range(0,len(s)):
        # 아스키 번호 차이를 이용해서 해당 배열 인덱스에 이미 알파벳이 있었는지 확인
        if flag[ord(s[i]) - ord('a')] == 1:  
            cnt += 1 # 이미 나온 알파벳이면 그룹 단어가 아니므로 cnt에 추가하고 반복문 종료
            break
        else: 
            # 처음 검색하는 알파벳이라면 앞문자와 같은지 확인
            if i > 0 and s[i-1] != s[i]: # 같지 않다면 해당 알파벳은 연속이 끝남남
                flag[ord(s[i-1]) - ord('a')] = 1 # 배열에 해당 알바펫이 나왔다는 마크 확인
            else: # 같다면 연속이므로 다음 인덱스 확인
             continue
    


print(N-cnt)