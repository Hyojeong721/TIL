import sys
from collections import deque
sys.stdin = open('input.txt')


def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        arr1 = merge_sort(left)
        arr2 = merge_sort(right)
        if arr1[-1] > arr2[-1]:
            cnt += 1

    return merge(arr1, arr2)


def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)
    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    arranged = merge_sort(numbers)
    print(f'#{tc} {arranged[N//2]} {cnt}')
