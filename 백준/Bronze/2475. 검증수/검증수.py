
# 리스트로 숫자 5개 받아오기기
numbers = list(map(int,input().split()))

# for문을 사용해서 리스트 요소들의 제곱값을 구하고 sum으로 합한 후 10의 나머지를 구함
ans = sum(n**2 for n in numbers) % 10

print(ans)