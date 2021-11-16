import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    # 가로 확인
    horizontal = 0
    for i in range(9):
        if len(set(matrix[i])) < 9:
            horizontal += 1

    # 세로 확인
    vertical = 0
    for j in range(9):
        check_column = []
        for i in range(9):
            check_column.append(matrix[i][j])
        if len(set(check_column)) < 9:
            vertical += 1

    # 9칸 확인
    box = 0
    border = [2, 5, 8]
    for i in border:
        for j in border:
            check_area = []
            for col in range(i, i-3, -1):
                for row in range(j, j-3, -1):
                    check_area.append((matrix[row][col]))
            if len(set(check_area)) < 9:
                box += 1

    if horizontal + vertical + box > 0:
        result = 0
    else:
        result = 1

    print(f'#{tc} {result}')

