# SWEA에선 안 돌아갑니다... ㅠ

import sys
sys.stdin = open('input.txt')
from collections import deque
import math
codes = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    answer = ''
    numbers = ''
    N, M = map(int, input().split())
    stack = ['0']
    dq = deque()
    lst = list(set([input() for _ in range(N)]))
    for pre_numbers in lst:
        numbers = ''
        for i in pre_numbers:
            numbers += format(int(i, 16), '04b')

        for j in numbers:
            if j != stack[0]:
                dq.append((stack[0], len(stack)))
                stack = [j]
            else:
                stack.append(stack[0])
    results = set()
    while dq:
        number = []
        for _ in range(8):
            dq.popleft()
            a = dq.popleft()[1]
            b = dq.popleft()[1]
            c = dq.popleft()[1]
            x = math.gcd(math.gcd(a, b), c)
            number.append(codes[(a // x, b // x, c // x)])
        results.add(tuple(number))

    answer = 0
    for i in results:
        tmp1 = 0
        tmp2 = 0
        for j in range(8):
            value = i[j]
            if j % 2 == 0:
                tmp1 += value
                tmp2 += 3 * value
            else:
                tmp1 += value
                tmp2 += value

        if tmp2 % 10 == 0:
            answer += tmp1

    print('#{} {}'.format(tc, answer))
