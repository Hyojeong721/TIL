import sys
sys.stdin = open("input.txt")

import collections

def bfs(me):
    cnt = 0
    my_f = [me]
    s = collections.deque()

    for i in range(T):
        if graph[me][i] == 'Y':
            my_f.append(i)
            s.append(i)
            cnt += 1

    while s:
        temp = s.popleft()
        for i in range(T):
            if i not in my_f and graph[temp][i] == 'Y':
                cnt += 1
                my_f.append(i)

    return cnt


T = int(input())
graph = [list(input()) for _ in range(T)]

res = 0
for i in range(T):
    res = max(res, bfs(i))

print(res)

