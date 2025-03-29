# 테스트 케이스 개수 입력
T = int(input())  # 여러 테스트 케이스를 처리하기 위해

# 각 테스트 케이스 처리
for _ in range(T):  
    N = int(input())  # 피보나치 수 N 입력
    
    # 0과 1의 출력 횟수를 저장할 배열 (DP 방식)
    count_0 = [0] * (N + 1)  # 0이 출력된 횟수를 저장하는 배열
    count_1 = [0] * (N + 1)  # 1이 출력된 횟수를 저장하는 배열

    # 초기값 설정 (기저 조건)
    count_0[0] = 1  # fibonacci(0) 호출 시 0이 1번 출력됨
    count_1[0] = 0  # fibonacci(0) 호출 시 1은 출력되지 않음
    
    if N > 0:  # N이 1 이상인 경우
        count_0[1] = 0  # fibonacci(1) 호출 시 0은 출력되지 않음
        count_1[1] = 1  # fibonacci(1) 호출 시 1이 1번 출력됨

    # 점화식으로 DP 테이블 채우기
    for i in range(2, N + 1):
        count_0[i] = count_0[i-1] + count_0[i-2]
        count_1[i] = count_1[i-1] + count_1[i-2]

    # 결과 출력: fibonacci(N)을 호출했을 때 0과 1이 출력된 횟수
    print(count_0[N], count_1[N])
