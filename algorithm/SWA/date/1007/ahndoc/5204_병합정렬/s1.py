import sys
sys.stdin = open('input.txt')

def merge(arr1, arr2):
    global cnt
    if arr1[len(arr1)-1] > arr2[len(arr2)-1]:
        cnt += 1
    result = []
    i = 0
    j = 0

    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        elif j < len(arr2):
            result.append(arr2[j])
            j += 1
    return result

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    arr = merge(left, right)

    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)[N//2]
    print('#{} {} {}'.format(tc, ans, cnt))