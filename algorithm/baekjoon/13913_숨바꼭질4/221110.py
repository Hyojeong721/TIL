import sys
input = sys.stdin.readline
from collections import deque

que = deque()
N, K = map(int, input().split())
visited = [False]*100001
visited[N]=True
que.append(([N], N, 0))
res = 1e9

while que:
    temp = deque()
    root, now, cnt = que.popleft()

    if now == K and cnt < res:
        res = cnt
        res_lst = root[:]
        continue



    temp = [now+1, now-1, now*2]
    for num in temp:
        root_temp = root[:]
        if num < 100001 and not visited[num]:
            if num >= K * 2 or num <= 0:
                continue
            else:
                root_temp.append(num)
                que.append((root_temp, num, cnt+1))
                visited[num] = True

print(res)
print(*res_lst)