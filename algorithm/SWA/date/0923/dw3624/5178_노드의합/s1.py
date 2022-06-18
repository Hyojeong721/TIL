import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0] + [0] * (N+1)

    for _ in range(M):
        n, num = map(int, input().split())
        nodes[n] = num

    for i in range(N//2, 0, -1):
        nodes[i] = nodes[i*2] + nodes[i*2+1]

    print('#{} {}'.format(tc, nodes[L]))