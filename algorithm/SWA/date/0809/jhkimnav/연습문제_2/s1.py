import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
matrix = []

for i in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

for i in range(N):
    total = 0
    for j in range(M):
        total += matrix[i][j]
    print(total)

# 버블 Sort 연습
# [55, 7, 78, 12, 42]
# a = [55, 7, 78, 12, 42]

# a = [0, 4, 1, 3, 1, 2, 4, 1]

# a, cnt각 배열의 원소값이 몇 개있는지 count
#  b = count 한 값 누적 배열
# 마지막 원