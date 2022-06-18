import sys
sys.stdin = open('input.txt')

def bin_search(l, r, number):
    """
    state 1: 이전에 오른쪽 탐색
    state 2: 이전에 왼쪽 탐색
    """
    state = 0
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] < number:
            if state == 1:
                return 0
            else:
                state = 1

            l = mid + 1
            continue
        elif lst[mid] > number:
            if state == 2:
                return 0
            else:
                state = 2
            r = mid - 1
            continue

        else:
            return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    B = list(map(int, input().split()))
    length = len(lst)
    lst.sort()
    total = 0
    for i in B:
        total += bin_search(0, length - 1, i)

    print('#{} {}'.format(tc, total))