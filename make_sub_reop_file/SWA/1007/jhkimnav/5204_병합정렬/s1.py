import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr) // 2
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])

        return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    global cnt

    result = []
    i = 0
    j = 0

    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sort_arr = merge_sort(arr)

    print('#{} {} {}'.format(tc, sort_arr[N//2], cnt))