import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
que = deque()
res = []
for i in range(1, N+1):
    que.append(i)
cnt = 0

while que:
    now = que.popleft()
    cnt += 1
    if cnt == K:
        res.append(now)
        cnt = 0
    else:
        que.append(now)
print("<", end = "",)
for r in range(N-1):
    print(res[r], end= ', ')
print(res[-1], end='')
print(">", end="")