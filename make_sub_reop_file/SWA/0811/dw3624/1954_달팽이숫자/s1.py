import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    mat = [[0] * n for _ in range(n)]

    val = 1
    row, col = 0, -1
    while n > 0:
        for right in range(n):
            col += 1
            mat[row][col] = val
            val += 1
        n -= 1

        for down in range(n):
            row += 1
            mat[row][col] = val
            val += 1

        for left in range(n):
            col -= 1
            mat[row][col] = val
            val += 1
        n -= 1

        for up in range(n):
            row -= 1
            mat[row][col] = val
            val += 1

    print('#{}'.format(t))
    for row in mat:
        for col in row:
            print(col, end = ' ')
        print()