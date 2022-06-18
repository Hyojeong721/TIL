# 재귀를 통한 구현
# 테스트케이스 10개 중 1개가 런타임 에러가 남.

import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    # 배열의 길이가 1 이하인 경우 => 배열을 그대로 반환한다.
    if len(arr) <= 1:
        return arr

    # 배열의 첫 번째 값을 pivot값으로 정한다.
    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input().split()]

    sorted_arr = quick_sort(arr)
    print("#{} {}".format(tc, sorted_arr[N // 2]))