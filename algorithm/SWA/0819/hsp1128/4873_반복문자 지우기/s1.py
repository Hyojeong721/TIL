# 2fail 런타임 에러
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chrs = list(input())
    stack = []
    stack.append(chrs.pop())

    while chrs:
        if len(chrs) > 1:
            if stack[-1] == chrs[-1]:
                stack.pop()
                chrs.pop()
            else:
                stack.append(chrs.pop())

        if len(chrs) == 1:
            if stack:
                if stack[-1] == chrs[-1]:
                    stack.pop()
                    chrs.pop()
                else:
                    stack.append(chrs.pop())
            else:
                stack.append(chrs.pop())
    print('#{} {}'.format(tc, len(stack)))

