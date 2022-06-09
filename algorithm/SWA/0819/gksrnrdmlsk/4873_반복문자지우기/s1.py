import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for i in text:
        if not len(stack) == 0:
            if not stack[-1] == i:
                stack.append(i)
            else:
                stack.pop()
        else: stack.append(i)

    print('#{} {}'.format(tc, len(stack)))