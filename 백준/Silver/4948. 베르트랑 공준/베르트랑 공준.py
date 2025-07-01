import sys
input = sys.stdin.readline

MAX = 123456 * 2
# 소수를 판단할 배열
is_prime = [True] * (MAX + 1)
# 0,1은 소수가 아니므로 false 초기화
is_prime[0] = is_prime[1] = False

 # 에라토스테네스의 체
# 2부터 최대값의 루트까지 검사
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        # 제곱부터 해당 인덱스의 배수인 인덱스들은 소수가 아님
        for j in range(i*i,MAX + 1,i):
            is_prime[j] = False

while(True):
    n = int(input()) 
    if n == 0:
        break
    else:
        # 소수 판정 배열에서 입력값 만큼 검사
        print(sum(is_prime[n+1:2*n+1]))
        continue




