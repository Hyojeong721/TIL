import sys
sys.stdin = open('input.txt')

T = int(input())


def check(text):
    brackets = ['(', ')', '{', '}']
    stack = []
    while text:
        letter = text.pop(0)
        if letter in brackets:
            stack.append(letter)

        if len(stack) > 0:
            try:
                if stack[-2:][0] == '(' and stack[-2:][1] == ')':
                    stack = stack[:-2]
                elif stack[-2:][0] == '{' and stack[-2:][1] == '}':
                    stack = stack[:-2]
            except IndexError:
                pass

    if len(stack) == 0:
        return 1
    else:
        return 0


for tc in range(1, T+1):
    text = list(input())
    result = check(text)
    print(f'#{tc} {result}')


