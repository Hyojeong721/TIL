import sys
sys.stdin = open('input.txt')
from collections import deque

n, K = map(int, input().split())
que = deque()
que.append(n)
MAX = 100001
visited = [0]*MAX

def bfs():

    while que:
        print(visited)
        x = que.popleft()
        if x==K:
            print(visited[x])
            exit(0)
        else:
            for new in (x+1, x-1, x*2):
                if 0 <= new < MAX and not visited[new]:
                    visited[new] = visited[x]+1
                    que.append(new)

bfs()

