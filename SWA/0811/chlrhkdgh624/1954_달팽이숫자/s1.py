import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    matrix = [[0]*N for _ in range(N)]

    numbers = list(range(1, N**2+1))

    for n in range(N):
        for j in range(N-n):
            if len(numbers) == 0:
                break
            else:
                matrix[n][j] = numbers.pop(0)
        for i in range(n+1, N-n):
            if len(numbers) == 0:
                break
            else:
                matrix[i][N-n-1] = numbers.pop(0)
        for j_ in range(N-n-2, 0, -1):
            if len(numbers) == 0:
                break
            else:
                matrix[N-n-1][j_] = numbers.pop(0)
        for i_ in range(N-n-1, 1, -1):
            if len(numbers) == 0:
                break
            else:
                matrix[i_][n] = numbers.pop(0)

    for i in range(N):
        for x in matrix[i]:
            print(x, end=' ')
        print()







