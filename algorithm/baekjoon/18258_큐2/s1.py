import sys
from collections import deque

N = int(sys.stdin.readline())
# N = int(input())
arr = deque()
for _ in range(N):
    con = list(sys.stdin.readline().split())
    # print(con)
    # con = list(input().split())
    size = len(arr)

    if len(con) == 2:
        arr.append(con[-1])
    elif con[0] == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif con[0] == 'size':
        print(size)
    elif con[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif con[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif con[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)

