'''

< 계산기 >

중위 표기법을 입력받아, 후위 표기법을 출력하는 프로그램

'''

import sys
sys.stdin = open('input2.txt')

string = input()
stack = []
top = -1
postfix = []

# isp: in-stack priority, icp: in-coming priority
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
operand = [str(i) for i in range(10)]

for token in string:
    # operator 이면, <- ')' 제외
    if token in icp:
        # 스택이 비어있거나, isp 보다 icp 가 크면 push
        if top == -1 or isp[stack[top]] < icp[token]:
            stack.append(token)
            top += 1
        # isp 보다 icp 가 작으면 pull
        elif isp[stack[top]] >= icp[token]:
            while True:
                if isp[stack[top]] >= icp[token]:
                    popped = stack.pop()
                    top -= 1
                    postfix.append(popped)
                else:
                    stack.append(token)
                    top += 1
                    break

    # operator 중 ')' 이면,
    elif token == ')':
        while True:
            popped = stack.pop()
            top -= 1
            if popped == '(':
                break
            else:
                postfix.append(popped)

    # operand 이면,
    elif token in operand:
        postfix.append(token)

# 수정
while stack:
    postfix.append(stack.pop())

print('postfix: {}'.format(postfix))
