


import sys
sys.stdin = open('input.txt')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    for idx, value in enumerate(lst[99]):
        if value == 2:
            final = idx
    r = 99
    c = final
    old_c = c
    old_r = r
    while r > 0 and 0 <= c <= 99:
        if old_c != c - 1 and lst[r][c - 1]:
            if lst[r][c - 1]:
                old_c = c
                old_r = r
                c -= 1

            else:
                old_c = c
                old_r = r
                r -= 1
                c -= 1

        elif old_c != c + 1 and lst[r][c + 1]:
            if lst[r][c + 1]:
                old_c = c
                old_r = r
                c += 1

            else:
                old_c = c
                old_r = r
                r -= 1
                c += 1

        else:
            old_c = c
            old_r = r
            r -= 1


    print('#{} {}'.format(tc, c))





    #
    # for c in [c for c in range(100) if lst[0][c] == 1]:
    #     i = 0
    #     j = 0
    #     while i <=100:





    # i = 0
    # j = -1
    # cnt = 0
    # while cnt < N * N:
    #     if 0 <= i + dx[k] <= N -1 and 0 <= j + dy[k] <= N -1 and lst[i + dx[k]][j + dy[k]] == 0:
    #         cnt += 1
    #         lst[i + dx[k]][j + dy[k]] = cnt
    #         i = i + dx[k]
    #         j = j + dy[k]
    #     else:
    #         k = (k + 1) % 4
    #
    # print('#{}'.format(tc))
    # for idx in range(N):
    #     print(' '.join(list(map(str, lst[idx]))))