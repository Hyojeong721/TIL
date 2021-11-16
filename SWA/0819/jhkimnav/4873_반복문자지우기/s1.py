import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    answer = 0
    stack = []
    string = input()
    for c in string:
        if len(stack) != 0 and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    answer = len(stack)
    print('#{} {}'.format(TC, answer))