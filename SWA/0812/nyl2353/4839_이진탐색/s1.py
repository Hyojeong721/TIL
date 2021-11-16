import sys
sys.stdin = open('input.txt')

def binary_search(total, finding):
    l = 1
    r = total
    cnt = 0

    while l <= r:
        c = int((l + r) / 2)
        if c == finding:
            return cnt
        elif c < finding:
            l = c
            cnt += 1
        else:
            r = c
            cnt += 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    P, A, B = list(map(int, input().split()))
    num_A = binary_search(P, A)
    num_B = binary_search(P, B)

    if num_A < num_B:
        winner = 'A'
    elif num_A > num_B:
        winner = 'B'
    else:
        winner = 0

    print('#{0} {1}'.format(tc, winner))