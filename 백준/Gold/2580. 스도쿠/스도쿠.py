# 입력
grid = [list(map(int, input().split())) for _ in range(9)]

# 행, 열, 블럭 체크 배열
rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
blocks = [[False] * 10 for _ in range(9)]

# 미리 채워진 숫자 반영
for i in range(9):
    for j in range(9):
        num = grid[i][j]
        if num != 0:
            rows[i][num] = True
            cols[j][num] = True
            blocks[(i // 3) * 3 + (j // 3)][num] = True

# 빈칸 리스트 미리 만들어두기 (백트래킹 성능 향상)
empty_cells = [
    (i, j)
    for i in range(9)
    for j in range(9)
    if grid[i][j] == 0
]

def backtrack(idx):
    if idx == len(empty_cells):
        return True  # 모든 칸 채웠으면 성공

    x, y = empty_cells[idx]
    block_idx = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        if not rows[x][num] and not cols[y][num] and not blocks[block_idx][num]:
            grid[x][y] = num
            rows[x][num] = cols[y][num] = blocks[block_idx][num] = True

            if backtrack(idx + 1):
                return True

            # 백트래킹
            grid[x][y] = 0
            rows[x][num] = cols[y][num] = blocks[block_idx][num] = False

    return False

# 실행
backtrack(0)

# 결과 출력
for row in grid:
    print(*row)
