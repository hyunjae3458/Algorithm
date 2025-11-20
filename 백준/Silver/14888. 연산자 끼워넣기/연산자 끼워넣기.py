N = int(input())
nums = list(map(int,input().split()))
# idx 0: 덧셈 개수, 1: 뺄셈 개수, 2: 곱셈 개수, 3: 나눗셈 개수
cal_tools = list(map(int,input().split()))

MAX = -int(1e9)
MIN = int(1e9)
cal_num = 0
# 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈
tool_lst = []
def calculate(cnt):
    global MAX
    global MIN
    if cnt == N-1:
        # 최소,최대 구하기
        sum_num = nums[0]
        for i in range(N-1):
            if tool_lst[i] == 0:
                sum_num += nums[i+1]
            if tool_lst[i] == 1:
                sum_num -= nums[i+1]
            if tool_lst[i] == 2:
                sum_num *= nums[i+1]
            if tool_lst[i] == 3:
                if sum_num < 0:
                    sum_num = -(abs(sum_num) // nums[i+1])
                else:
                    sum_num //= nums[i+1]
        MAX = max(MAX,sum_num)
        MIN = min(MIN,sum_num)
        return 
    for i in range(4):
        if cal_tools[i] != 0:
            cal_tools[i] -= 1
            tool_lst.append(i)
            calculate(cnt+1)
            cal_tools[i] += 1
            tool_lst.pop()

calculate(0)
print(MAX)
print(MIN)