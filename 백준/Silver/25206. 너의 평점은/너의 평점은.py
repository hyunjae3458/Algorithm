
out_put = []
# 과목평점을 담을 딕션어리리
rate = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

# 전공과목별의 합합
total_rate = 0

# 리스트 안에 입력값을  공백 별로 나눈 문자열들을 요소로 갖는 리스트로 받아온다
for i in range(20):
    out_put.append(list(input().split()))

#  s[0] = 과목 이름, s[1] = 과목 학점 , s[2] = 과목평점점
for s in out_put:
    # 만약 p가 있으면 무시
    if s[2] == "P":
        continue
    else: # 학점 x 과목평점들의 합합
        total_rate += float(s[1]) * rate[s[2]]

# 전공평점을 구한다다
major_rate = float(total_rate / sum(float(j[1]) for j in out_put if j[2] != "P"))

# 소수점 6자리까지 출력
print("{:0.6f}".format(major_rate))