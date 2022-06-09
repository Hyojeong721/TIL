import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()
    # 첫 번째 문자 push
    stack = [text[0]]

    # 해당 문자가 stack 에 마지막으로 넣었던 값과 동일하면 pop, 아니면 push.
    for i in range(1, len(text)):
        if len(stack) and stack[-1] == text[i]:
            stack.pop()
        else:
            stack.append(text[i])

    print('#{0} {1}'.format(tc, len(stack)))