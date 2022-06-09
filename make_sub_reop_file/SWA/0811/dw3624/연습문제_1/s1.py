import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for row in range(n):
        for col in range(n):
            a,b,c,d = 0, 0, 0, 0
            if row != 0:
                # 위 값과의 차이
                a = matrix[row][col] - matrix[row-1][col]
            if row != n - 1:
                # 아래 값과의 차이
                b = matrix[row][col] - matrix[row+1][col]
            if col != 0:
                # 외쪽 값과의 차이
                c = matrix[row][col] - matrix[row][col-1]
            if col != n - 1:
                # 오른쪽 값과의 차이
                d = matrix[row][col] - matrix[row][col+1]

            result += abs(a) + abs(b) + abs(c) + abs(d)
    print(result)
