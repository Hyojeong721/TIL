import sys
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin.readline().split())
matrix = []

# 2차원 배열 입력받기
for i in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

# (N, M)의 2차원 배열 인덱스로 접근하기
for i in range(N):
    total = 0
    for j in range(M):
        total += matrix[i][j]
    print(total)
