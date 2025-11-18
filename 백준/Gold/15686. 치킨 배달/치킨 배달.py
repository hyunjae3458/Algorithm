from itertools import combinations
import sys
INIT_MIN = sys.maxsize
input = sys.stdin.readline

N,M = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

apt_lst = []
chickens = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            apt_lst.append((i,j))
        if grid[i][j] == 2:
            chickens.append((i,j))

chicken_combs = list(combinations(chickens,M))

min_chicken_dist = INIT_MIN
for chicken_comb in chicken_combs:
    dist_lst = []
    for apt_x,apt_y in apt_lst:
        min_dist = INIT_MIN
        for i in range(M):
            dist = abs(apt_x - chicken_comb[i][0]) + abs(apt_y-chicken_comb[i][1])
            min_dist = min(min_dist,dist)
        dist_lst.append(min_dist)
    min_chicken_dist = min(min_chicken_dist,sum(dist_lst))


print(min_chicken_dist)

    