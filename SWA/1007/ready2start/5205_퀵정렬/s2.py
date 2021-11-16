# 재귀 구현의 런타임 에러가 최대 재귀호출 횟수를 초과했기 때문이라고 추측하여,
# 재귀 대신 스택을 활용한 DFS 방식으로 구현했으나, 같은 에러가 남.

import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    global sorted_arr
    stack = []
    stack.append(arr)

    while stack:
        current = stack.pop()

        # 배열의 길이가 1 이하인 경우 => 해당 배열을 sorted_arr에 더한다.
        if len(current) <= 1:
            sorted_arr.extend(current)
            continue

        # 배열의 첫 번째 값을 pivot값으로 정한다.
        pivot = current[0]
        left = []
        right = []

        for i in range(1, len(current)):
            if current[i] <= pivot:
                left.append(current[i])
            else:
                right.append(current[i])

        stack.append(right)
        stack.append([pivot])
        stack.append(left)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input().split()]
    sorted_arr = []

    quick_sort(arr)
    print("#{} {}".format(tc, sorted_arr[N // 2]))
