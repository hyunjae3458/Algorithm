def calculate_prize(dice1, dice2, dice3):
    dice = [dice1, dice2, dice3]
    dice.sort()  # 정렬하여 비교를 쉽게 하기

    if dice[0] == dice[1] == dice[2]:  # 같은 눈 3개
        return 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[1] == dice[2]:  # 같은 눈 2개
        return 1000 + dice[1] * 100
    else:  # 모두 다른 눈
        return max(dice) * 100

# 입력 받기
dice1, dice2, dice3 = map(int, input().split())

# 결과 출력
print(calculate_prize(dice1, dice2, dice3))
