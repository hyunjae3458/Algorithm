import sys
input = sys.stdin.readline

# 문자열 채우는 재귀함수
def solve(n):
    # 만약 n이 길이가 1이되면 "-"으로 문자열 반환
    if n == 1:
        return "-"

    # "-"" 로 채울 문자열
    left = solve(n // 3)
    # 가운데 빈칸으로 채울 문자열
    center = " " * (n // 3)

    # 문자열 반환
    return left + center + left 

# 입력에 제한을 두지 않기 때문에 try except로 EOF예외처리
while True: 
    try:
        N = int(input())
        # 재귀
        ans = solve(3**N)
        
        print(ans)
    except:
        break
    



