import sys
sys.stdin = open('input.txt')


def binary_search(arr, k):
    start, end = 0, len(arr) - 1
    direction = ''

    while start <= end:
        mid = (start + end) // 2

        # k를 찾은 경우 => count를 1 증가시키고 탐색 종료
        if arr[mid] == k:
            global count
            count += 1
            return
        elif arr[mid] > k:
            # 같은 방향을 2번 연속 탐색 => 탐색 종료
            if direction == 'left':
                return
            end = mid - 1
            direction = 'left'
        else:
            # 같은 방향을 2번 연속 탐색 => 탐색 종료
            if direction == 'right':
                return
            start = mid + 1
            direction = 'right'


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [int(x) for x in input().split()]
    numbers = [int(x) for x in input().split()]
    count = 0

    arr.sort()

    for number in numbers:
        binary_search(arr, number)

    print("#{} {}".format(tc, count))
