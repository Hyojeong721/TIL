import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str = input()
    stack = []
    for i in range(len(str)):
        if stack and stack[-1] == str[i]:
            stack.pop()
        else:
            stack.append(str[i])

    print('#{} {}'.format(tc,len(stack)))