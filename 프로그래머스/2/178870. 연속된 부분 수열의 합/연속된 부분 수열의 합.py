def solution(sequence, k):
    answer = [0,len(sequence)]
    L = 0
    R = 0
    sum_num = sequence[L]
    while True:
        if sum_num < k:
            R += 1
            if R == len(sequence):
                break
            sum_num += sequence[R]
        else:
            if sum_num == k:
                if R-L < answer[1] - answer[0]:
                    answer = [L,R]            
            sum_num -= sequence[L]
            L += 1
    return answer