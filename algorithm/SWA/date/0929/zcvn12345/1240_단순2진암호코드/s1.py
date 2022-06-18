import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    secret = [input() for _ in range(N)]
    code = ''
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if secret[i][j] == '1':
                for x in range(56):
                    code += secret[i][j-x]
                break

    print(code)

