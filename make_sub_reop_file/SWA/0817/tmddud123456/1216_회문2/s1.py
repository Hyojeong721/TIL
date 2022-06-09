import sys
sys.stdin = open('input.txt')


def asdf():
    global matrix
    for i in range(99, 2, -1):
        for j in range(0, 100 - i):
            for k in range(0, 100):
                if matrix[j][k] == matrix[j + i][k]:
                    l = 0
                    count = 0
                    while j + l < j + i -l:
                        if matrix[j + l][k] == matrix[j + i -l][k]:
                            count += 2
                        l += 1
                    if count >= i :
                        return i + 1
                if matrix[k][j] == matrix[k][j + i]:
                    l = 0
                    count = 0
                    while j + l < j + i -l:
                        if matrix[k][j + l] == matrix[k][j + i -l]:
                            count += 2
                        l += 1
                    if count >= i :
                        return i + 1

for tc in range(1, 11):
    T = int(input())
    matrix = []
    for i in range(100):
        row_matrix = list(map(str, input()))
        matrix.append(row_matrix)
    print(f'#{T} {asdf()}')



