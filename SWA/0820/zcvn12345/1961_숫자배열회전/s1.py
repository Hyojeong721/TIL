import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(input().split()))

    result = [[] for _ in range(N)]

    for i in range(N):
        nums = ''
        for j in range(N-1, -1, -1):
            nums += matrix[j][i]
        result[i].append(nums)

    for i in range (N-1, -1, -1):
        nums = ''
        for j in range(N-1, -1, -1):
            nums += matrix[i][j]
        result[N-1-i].append(nums)

    for i in range (N-1, -1, -1):
        nums = ''
        for j in range(N):
            nums += matrix[j][i]
        result[N-1-i].append(nums)
    print('#{0}'.format(tc))
    for i in range(N):
        for j in result[i]:
            print(j, end = ' ')
        print()