# numbers 리스트를 오름차순 정렬
# 마지막 0의 idx부터의 거리
# numbers 리스트의 마지막 요소의 idx와 0의 idx의 차이 반환

import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    for idx, number in enumerate(numbers):
        if number == 0:
            zero_idx = idx
        else:
            break

    result = n - zero_idx + 1

    print('#{} {}'.format(t, result))
