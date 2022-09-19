import sys
T = int(sys.stdin.readline())
from collections import deque


for t in range(T):
    arr = deque()
    N, M = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    chr_cnt = 65
    for n in range(N):
        arr.append((chr(chr_cnt), temp[n]))
        chr_cnt += 1

    target = arr[M][0]

    cnt = 0
    go = False
    while cnt < N and not go:
        now = arr.popleft()
        size = len(arr)
        for k in range(size):
            if arr[k][1] > now[1]:
                arr.append(now)
                break
        else:
            if target == now[0]:
                print(cnt+1)
                go = True
                break
            cnt += 1