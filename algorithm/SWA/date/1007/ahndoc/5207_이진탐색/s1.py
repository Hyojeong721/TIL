import sys
sys.stdin = open('input.txt')

def binary_search(arr, k):
    low = 0
    high = len(arr) - 1
    state = 0
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == k:
            return middle

        elif arr[middle] > k:
            if state == 0 or state == 'right':
                state = 'left'
                high = middle - 1
            else:
                return -1
        else:
            if state == 0 or state == 'left':
                state = 'right'
                low = middle + 1
            else:
                return -1
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in B:
        if binary_search(A, i) != -1:
            ans += 1

    print('#{} {}'.format(tc, ans))