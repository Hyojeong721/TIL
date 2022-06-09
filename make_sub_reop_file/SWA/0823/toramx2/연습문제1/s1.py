import sys
sys.stdin = open('input.txt')


infix = list(input().split())
postfix = []
stack = []
num = '0123456789'

for a in infix:
    if a in num:
        postfix.append(a)
    else:
        pass


for i in range(len(infix), -1, -1):
    postfix.append(stack[i])

print(*postfix)