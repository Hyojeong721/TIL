import sys
sys.stdin = open('input.txt')

A = input()

stack = []
for a in A:
    if a in '+-=/*':
        stack.append(a)
    else:
        print(a, end='')
for i in range(len(stack)):
    s = stack.pop()
    print(s, end='')
