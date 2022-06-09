import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    lst = [([0] + list(map(int, input().split())) + [0]) for _ in range(100)]
    for idx, value in enumerate(lst[99]):
        if value == 2:
            final = idx
    r = 99
    c = final

    while r > 0 and 1 <= c <= 100:
        if lst[r][c - 1]:
            if lst[r][c - 2]:
                lst[r][c] = 0
                c -= 1

            else:
                r -= 1
                c -= 1

        elif lst[r][c + 1]:
            if lst[r][c + 2]:
                lst[r][c] = 0
                c += 1

            else:
                r -= 1
                c += 1

        else:
            r -= 1


    print('#{} {}'.format(tc, c - 1))