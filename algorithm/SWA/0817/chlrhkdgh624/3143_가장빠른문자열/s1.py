import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    test, speed = list(input().split())
    N, M = len(test), len(speed)
    count = 0
    i = 0  # test index
    j = 0  # speed index

    while i < N and j < M:
        if test[i] != speed[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == M:
            count += 1
            j = 0
            i -=1

    print(f'#{tc} {N - count*M + count}')