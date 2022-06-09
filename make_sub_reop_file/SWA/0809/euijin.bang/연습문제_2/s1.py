import sys
sys.stdin = open('input.txt')

row, col = map(int, input().split())

# 2차원 배열 각 행의 합 구하기

# 2차원 배열 입력받기
arr = [list(map(int, input().split())) for _ in range(row)]

# (row, col)의 2차원 배열 인덱스로 접근하기
for i in range(row):
    row_total = 0
    for j in range(col):
        row_total += arr[i][j]
    print(row_total)