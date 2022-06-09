import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    while cnt < M:
        v = data.pop(0)
        data.append(v)
        cnt += 1
    print('#{} {}'.format(tc, data[0]))