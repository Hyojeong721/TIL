import sys
sys.stdin = open('input.txt')

def findCode():
    global N, M, matrix
    pass_code = []
    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] != '0':
                pass



TC = int(input())

for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        temp = list(map(str, input()))
        matrix.append(temp)
    print(matrix)
