import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
# 배열을 한행씩 받아온다.
for i in range(N):
    matrix_total = 0
    matrix = list(map(int, input().split()))
    # 행의 모든 요소 값을 더해준다.
    for j in range(M):
        matrix_total += matrix[j]
    print(matrix_total)
