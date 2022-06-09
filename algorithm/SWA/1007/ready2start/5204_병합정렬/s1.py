import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    # 배열의 길이가 1 이하인 경우 => 배열을 그대로 반환한다.
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    # i : left 배열의 탐색 위치 / j : right 배열의 탐색 위치
    i, j = 0, 0
    new_arr = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    # 오른쪽 배열의 정렬이 먼저 끝난 경우 = 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
    if i < len(left):
        new_arr.extend(left[i:])
        global count
        count += 1
    # 왼쪽 배열의 정렬이 먼저 끝난 경우
    else:
        new_arr.extend(right[j:])

    return new_arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input().split()]
    count = 0

    sorted_arr = merge_sort(arr)
    print("#{} {} {}".format(tc, sorted_arr[N // 2], count))
