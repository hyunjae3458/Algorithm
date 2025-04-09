import sys
N = int(input())

# 단어개수 저장
cnt = 0 
out_put = []


for _ in range(N):
    out_put.append(input())

# ord() -> 아스키 순서 표현
for s in out_put:
    arr = [0] * 26
    for i in range(0,len(s)):
        if arr[ord(s[i]) - ord('a')] == 1:
            cnt += 1
            break
        else:
            if i > 0 and s[i-1] != s[i]:
                arr[ord(s[i-1]) - ord('a')] = 1
            else:
             continue
    


print(N-cnt)