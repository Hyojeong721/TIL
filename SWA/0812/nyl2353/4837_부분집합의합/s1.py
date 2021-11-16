import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))

    subset_num = 0
    for i in range(1 << 12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += j + 1
        if cnt == N and total == K:
            subset_num += 1

    print('#{0} {1}'.format(tc, subset_num))