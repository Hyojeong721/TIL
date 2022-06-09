import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = 0

    while cnt < M:
        tmp = data.pop(0)
        data.append(tmp)
        cnt += 1

    print('#{} {}'.format(t, data[0]))