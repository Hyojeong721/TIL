import sys
input = sys.stdin.readline
from collections import deque

que = deque()
N, K = map(int, input().split())
visited = [False]*100001
visited[N] = True
res_lst = str(N)+','
que.append((res_lst, N, 0))
res = 1e9

while que:
    temp = deque()
    root, now, cnt = que.popleft()
    if now == K and cnt < res:
        res = cnt
        res_lst = root
        continue

    temp = [now+1, now-1, now*2]
    for num in temp:
        root_temp = root
        if 0 <= num <= 100000 and not visited[num]:
            root_temp = root_temp + str(num) + ','
            que.append((root_temp, num, cnt+1))
            visited[num] = True

print(res)
print(*res_lst.split(',')[:-1])
