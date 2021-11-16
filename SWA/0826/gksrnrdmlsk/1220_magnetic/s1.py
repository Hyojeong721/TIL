# 스택!

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if r > c:
                lst[r][c], lst[c][r] = lst[c][r], lst[r][c]
    cnt = 0
    for r in range(N):
        stack = []
        for c in lst[r]:
            if c:
                if not stack and c == 2:
                    continue
                stack.append(c)

        for i in range(len(stack) - 1):
            if stack[i] == 1 and stack[i + 1] == 2:
                cnt += 1

    print('#{} {}'.format(tc, cnt))