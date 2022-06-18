import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):

    stack = []
    text = input()

    # 짝꿍을 만나면 손잡고 나가라.
    for char in text:
        stack.append(char)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))