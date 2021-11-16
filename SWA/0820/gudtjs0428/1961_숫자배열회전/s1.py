import sys
sys.stdin = open('input.txt')

def revolve_matrix(matrix):
    result = [[] for _ in range(len(matrix))]
    n = 0
    for j in range(len(matrix)):
        tmp = ''
        for i in range(len(matrix)-1, -1, -1):
            tmp += matrix[i][j]
        result[n].append(tmp)
        tmp = ''
        n += 1
    n = 0
    for i in range(len(matrix)-1, -1, -1):
        tmp = ''
        for j in range(len(matrix)-1, -1, -1):
            tmp += matrix[i][j]
        result[n].append(tmp)
        tmp = ''
        n += 1
    n = 0
    for j in range(len(matrix)-1, -1, -1):
        tmp = ''
        for i in range(len(matrix)):
            tmp += matrix[i][j]
        result[n].append(tmp)
        tmp = ''
        n += 1
    n = 0
    return result


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]
    print('#{}'.format(test_case))
    result = revolve_matrix(matrix)
    for i in range(N):
        for j in range(3):
            print(result[i][j], end=' ')
        print()