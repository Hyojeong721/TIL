import sys
sys.stdin = open('input.txt')

def get_fast_search(binary_search_info):
    l = 1
    r = binary_search_info[0]
    c = int((l + r) / 2)
    A = binary_search_info[1]
    B = binary_search_info[2]
    count_A = 1
    count_B = 1
    while A != c:
        count_A += 1
        if A > c:
            l = c
        else :
            r = c
        c = int((l + r) / 2)

    l = 1
    r = binary_search_info[0]
    c = int((l + r) / 2)
    while B != c:
        count_B += 1
        if B > c:
            l = c
        else :
            r = c
        c = int((l + r) / 2)

    if count_A < count_B:
        return 'A'
    elif count_A == count_B:
        return 0
    else:
        return 'B'


T = int(input())
for tc in range(1, T + 1):
    binary_search_info = list(map(int, input().split()))
    print('#{} {}'.format(tc, get_fast_search(binary_search_info)))