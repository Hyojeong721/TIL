import sys
sys.stdin = open("input.txt")

def func1(str1):
    stack=[]
    for i in str1:
        if i == '{' or i == '(':
            stack.append(i)

        elif i == '}':
            if len(stack)>0 and stack[-1] == '{':
                stack.pop()
            else:
                return 0

        elif i == ')':
            if len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0

    if len(stack) > 0:
        return 0
    elif len(stack) ==0:
        return 1

T=int(input())
for tc in range(1,T+1):
    str1=[]
    str_input=input()
    for i in str_input:
        str1.append(i)

    print('#{} {}'.format(tc,func1(str1)))
