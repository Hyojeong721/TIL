import sys
sys.stdin = open('input.txt', 'r')


def binary_search(left, right, key, arr2):
    global cnt
    mid = (left + right) // 2

    if list_a[mid] == key:
        cnt += 1
        return

    if left >= right:
        return

    if key < list_a[mid]:
        if arr2 and arr2[-1] == 'right':
            arr2.append('left')
            return binary_search(left, mid-1, key, arr2)
    else:
        if arr2 and arr2[-1] == 'left':
            arr2.append('right')
            return binary_search(mid+1, right, key, arr2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    cnt = 0
    for x in list_b:
        move = []
        binary_search(0, N-1, x, move)
    print(f'#{tc} {cnt}')
