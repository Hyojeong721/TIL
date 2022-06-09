'''

< 괄호 없는 계산기 >

중위 표기법을 입력받아, 후위 표기법을 출력하는 프로그램

'''

import sys
sys.stdin = open('input.txt')

string = input()    # 입력받은 문자열
stack = []          # operator 저장할 stack
operand = [str(i) for i in range(10)]   # operand 범위: 0~9
operator = ['+', '-', '*', '/']         # operator: 사칙연산

# operand 는 바로 출력, operator 는 stack 에 push
for char in string:
    if char in operand:
        print(char, end=' ')
    elif char in operator:
        stack.append(char)

# stack 에 남아있는 연산자를 모두 pop 하여 출력
while stack:
    print(stack.pop(), end=' ')