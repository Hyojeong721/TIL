import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chrs = list(input())
    stack = []

    for i in range(len(chrs)):
        if len(stack) == 0:
            stack.append(chrs[i])
        else:
            if stack[-1] == chrs[i]:
                stack.pop()
            else:
                stack.append(chrs[i])
    print('#{} {}'.format(tc, len(stack)))




