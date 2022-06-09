# P16
# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자

import sys
sys.stdin = open('input.txt')

def if_part_sum_zero(nums):
    n = len(nums)
    parts = []
    part = []
    for i in range(1<<n):       # i가 0부터 2진수로 (2 ** n) - 1 동안
        for j in range(n):      # j 가 0 ~ n 까지
            if i & (1<<j):      # i 와 2진수 2 ** j
                part.append(nums[j])
        parts.append(part)
        part = []

    check = 0
    for i in range(1, len(parts)):
        total = 0
        for num in parts[i]:
            total += num
        if total != 0:
            pass
        else:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc, if_part_sum_zero(nums)))