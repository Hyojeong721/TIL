# 재귀 구현의 런타임 에러가 새로운 정렬을 만드는 것에 따른 메모리 초과 때문이라고 추측하여,
# 원본 배열 내에서 수들을 정렬하는 정석적인 방식으로 구현하여 통과함.

import sys
sys.stdin = open('input.txt')


def quick_sort(left, right):
    global arr

    if left >= right:
        return

    # 배열의 첫 번째 값을 pivot값으로 정한다.
    pivot = left
    i, j = left + 1, right

    while i <= j:
        # 왼쪽에서 피벗보다 큰 값의 인덱스를 찾는다.
        while i <= j and arr[i] <= arr[pivot]:
            i += 1

        # 오른쪽에서 피벗보다 작은 값의 인덱스를 찾는다.
        while i <= j and arr[j] >= arr[pivot]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    quick_sort(left, j - 1)
    quick_sort(j + 1, right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input().split()]
    sorted_arr = []

    quick_sort(0, N - 1)
    print("#{} {}".format(tc, arr[N // 2]))
