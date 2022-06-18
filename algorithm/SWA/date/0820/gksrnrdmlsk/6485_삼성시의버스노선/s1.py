import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = [0] * 5001
    N = int(input())
    for _ in range(N):
        i, j = map(int, input().split())
        for k in range(i, j + 1):
            lst[k] += 1

    P = int(input())
    stops = [int(input()) for _ in range(P)]
    result = ' '.join(map(str, [lst[i] for i in stops]))
    print('#{} {}'.format(tc, result))