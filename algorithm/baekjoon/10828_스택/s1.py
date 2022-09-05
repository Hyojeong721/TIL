
import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for n in range(N):
    arr = sys.stdin.readline().split()
    if len(arr) > 1:
        stack.append(int(arr[1]))
    elif arr[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(stack))
    elif arr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif arr[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)