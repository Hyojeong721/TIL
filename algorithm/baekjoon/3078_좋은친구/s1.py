import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = deque()

for n in range(N):
    now = sys.stdin.readline()
    arr.append(now)

cnt = 0
for i in range(N):
    now = arr[i]
    for k in range(1, K+1):
        if 0 <= i+k < N and len(now) == len(arr[i+k]):
            cnt += 1

print(cnt)