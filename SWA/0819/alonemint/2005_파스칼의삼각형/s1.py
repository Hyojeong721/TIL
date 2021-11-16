import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):

    N = int(input())

    triangle = [[1], [1, 1]]
    for i in range(2, N):
        tmp = []
        tmp.append(1)

        for j in range(i - 1):
            tmp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        tmp.append(1)

        triangle.append(tmp)
    print('#{}'.format(tc))
    for row in triangle[:N]:
        for element in row:
            print(element, end = ' ')
        print()


