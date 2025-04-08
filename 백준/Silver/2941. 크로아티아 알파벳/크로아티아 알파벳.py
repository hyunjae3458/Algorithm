problem_string = input() # 문자열 입력 받기

cnt = len(problem_string) # 문자열 문자 개수 만큼 추가가

croa_alpha = ["c=", "c-" ,"dz=" , "d-", "lj", "nj", "s=", "z="]


for i in croa_alpha: # 리스트에 있는 문자가 나올때마다 cnt에서 -1씩 한다
    if i in problem_string:
        cnt -= 1 * problem_string.count(i)
    
print(cnt)