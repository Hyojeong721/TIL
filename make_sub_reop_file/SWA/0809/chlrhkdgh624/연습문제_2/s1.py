import sys

sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
print(N, M)

matrix = []

for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)

for i in range(N):
    total = 0
    for j in range(M):
        print(i, j, matrix[i][j])
        total += matrix[i][j]
    print('---', total)