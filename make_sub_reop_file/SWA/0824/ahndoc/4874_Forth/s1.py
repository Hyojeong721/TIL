import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    data = list(input().split())

    stack = []
    for i in data:

        try:
            if i == '.' and len(stack) == 1:
                result = str(stack.pop())
                break

            if i == '.' and len(stack) >= 2:
                result = 'error'
                break

            if type(int(i)) is int:
                stack.append(int(i))

        except:
            if i == '+':
                try:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 + num2)
                except:
                    result = 'error'
                    break
            elif i == '-':
                try:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)
                except:
                    result = 'error'
                    break
            elif i == '*':
                try:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 * num2)
                except:
                    result = 'error'
                    break
            elif i == '/':
                try:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 // num2)
                except:
                    result = 'error'
                    break
            else:
                result = 'error'
                break
    print('#{} {}'.format(tc, result))

#####################################################
# for tc in range(1, T + 1):
#     data = list(input().split())
#
#     stack = []
#
#     task_list = ['+', '-', '*', '/']
#
#     for i in data:
#         if i in task_list:
#             if len(stack) == 1:
#                 result = 'error'
#                 break
#             num2 = int(stack.pop())
#             num1 = int(stack.pop())
#             if i == '+':
#                 temp = num2 + num1
#             elif i == '-':
#                 temp = num2 + num1
#             elif i == '*':
#                 temp = num2 + num1
#             elif i == '/':
#                 temp = num2 + num1
#             stack.append(temp)
#         elif i == '.':
#             if len(stack) == 1:
#                 result = stack.pop()
#             else:
#                 result = 'error'
#                 break
#         else:
#             stack.append(i)
#     print('#{} {}'.format(tc, result))