import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    res = 'YES'
    stack = []
    arr = list(input())
    for k in arr:
        if k == '(':
            stack.append(k)
        elif k == ')':
            if stack:
                stack.pop()
            else:
                res = 'NO'
                break
    else:
        if stack:
            res = 'NO'

    print(res)