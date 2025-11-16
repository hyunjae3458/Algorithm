import sys
input = sys.stdin.readline

wheel_lst = [
    list(map(int,input().strip()))
    for _ in range(4)
]

K = int(input())

commands = [
    list(map(int,input().split()))
    for _ in range(K)
]

dp = [
    [-1] * 9
    for _ in range(4)
]

def in_range(x):
    return x >= 0 and x < 4

for wheel_num,wheel in enumerate(wheel_lst):
    for idx, dir in enumerate(wheel):
        dp[wheel_num][(idx + 3) % 8 or 8] = dir

def timeDir(wheel,wheel_num):
    temp = wheel[wheel_num][-1]
    for i in range(len(wheel[wheel_num]) - 1,0,-1):
        wheel[wheel_num][i] = wheel[wheel_num][i - 1]
    wheel[wheel_num][1] = temp

def anti_timeDir(wheel,wheel_num):
    temp = wheel[wheel_num][1]
    for i in range(1,len(wheel[wheel_num]) - 1):
        wheel[wheel_num][i] = wheel[wheel_num][i + 1]
    wheel[wheel_num][-1] = temp


for wheel_num, dir in commands:
    wheel_num = wheel_num - 1
    rotate = [0]*4
    rotate[wheel_num] = dir 

    # 연쇄되어 움직이는 체크하는 리스트
    # 왼쪽 전파
    for i in range(wheel_num-1,-1,-1):
        if dp[i+1][1] != dp[i][5]:
            rotate[i] = -rotate[i+1]
        else:
            break
    #오른쪽 전파
    for i in range(wheel_num + 1,4):
        if dp[i-1][5] != dp[i][1]:
            rotate[i] = -rotate[i-1]
        else:
            break
    
    for wheel_num, dir in enumerate(rotate):
        if dir == -1:
            anti_timeDir(dp,wheel_num)
        elif dir == 1:
            timeDir(dp,wheel_num)


score = 0
for i in range(4):
    if dp[i][3] == 1:
        score += 2**i

print(score)