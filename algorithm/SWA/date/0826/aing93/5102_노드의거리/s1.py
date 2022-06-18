import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    visited = [[0] * V+1 for _ in range(V+1)]
    result = 0
def bfs(S, G):
    queue = [S]
    visited[S] = 1
    while len(queue):
        front = queue.pop(0)

        if front == G:
            print('a')
            return
        if not visited[front]:
            visited[front] = 1

            for j in range(V+1):
                if graph[front][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    result[j] = result[front] + 1

