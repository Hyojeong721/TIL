import sys
sys.stdin = open('input.txt')

T = int(input())


def bfs(v):
    global result
    queue = []
    queue1 = [0]
    queue.append(v)

    while queue:
        v = queue.pop(0)
        visited[v] = 1
        idx = queue1.pop(0)
        for i in range(E):
            if arr[i][0] == v and visited[arr[i][1]] == 0:
                queue.append(arr[i][1])
                queue1.append(idx+1)

            if arr[i][1] == v and visited[arr[i][0]] == 0:
                queue.append(arr[i][0])
                queue1.append(idx+1)
        if G in queue:
            result = queue1[-1]
            return


for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드 개수, 간선 개수
    arr = []
    visited = [0] * (V+1)

    for e in range(E):
        arr.append(list(map(int, input().split())))

    S, G = map(int, input().split())  # 출발, 도착
    result = 0

    bfs(S)

    print('#{} {}'.format(tc, result))

