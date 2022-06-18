import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = ''
    for letter in text:
        stack += letter
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack = stack[:-2]

    print(f'#{tc} {len(stack)}')
