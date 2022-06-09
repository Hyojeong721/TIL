import sys
sys.stdin = open('input.txt')

def read(n):
    global answer
    if n <= N:
        # left
        read(n * 2)

        # root
        answer += nodes[n]

        # right
        read(n * 2 + 1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    nodes = [0] * (N+1)


    for _ in range(N):
        tmp = list(input().split())
        n = int(tmp[0])
        char = tmp[1]
        nodes[n] = char


    answer = ''
    read(1)
    print('#{} {}'.format(tc, answer))