import sys
open = sys.stdin.readline()

stack = []
while True:
    n = input()
    if n == '문제':
        stack.append('문제')
    elif n == '고무오리':
        if stack:
            stack.pop()
        else:
            stack.append('문제')
            stack.append('문제')
    elif n == '고무오리 디버깅 끝':
        if stack:
            print('힝구')
        else:
            print('고무오리야 사랑해')
        break
