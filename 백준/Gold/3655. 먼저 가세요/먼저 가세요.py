import sys
input = sys.stdin.readline

a = int(input())


# 문자열의 값과 인덱스를 받아서 딕션어리에 저장
for _ in range(a):
    group = {}
    n_len = int(input())
    n = input()
    for idx,char in enumerate(n):
        if char not in group:
            # 딕션어리 값으로 인덱스와 사람 수 저장
            group[char] = [1,idx]
        else:
            # 있으면 한명 추가, 인덱스 갱신
            group[char][0] += 1
            group[char][1] = idx
            
    # 리스트로 그룹명, 인원수, 마지막 인덱스를 집합으로 저장 
    group_list = []
    for char, (i, idx) in group.items():
        group_list.append((idx, i, char))

    # 마지막 인덱스 순으로 오름차순 정렬
    group_list.sort()

    # 아지 아무도 안섰을때는 인덱스가 -1이므로 
    cur_idx = -1
    ans  = 0
    for idx,i,char in group_list:
        # 현재의 인덱스 구함
        cur_idx += i
        # 절약되는 시간 = (마지막 인덱스 - 정렬 후 마지막 인덱스) * 인원수 * 5
        save = (idx - cur_idx) * i * 5  
        ans += save

    print(ans)

