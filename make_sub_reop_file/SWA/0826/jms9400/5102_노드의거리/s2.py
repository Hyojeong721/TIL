import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드 개수, 간선 개수
    arr = []
    queue = []  # 가야할 노드
    queue1 = [0]  # 지나간 간선의 개수
    visited = [0] * (V+1)  # 방문한 노드

    for e in range(E):
        arr.append(list(map(int, input().split())))

    S, G = map(int, input().split())  # 출발, 도착
    queue.append(S)

    result = 0

    # 너비 우선 탐색(bfs)
    while queue:  # result == 0이 안되는 이유: 결과값이 최종적으로 0이되는 경우
        S = queue.pop(0)
        visited[S] = 1
        idx = queue1.pop(0)
        for i in range(E):
            if arr[i][0] == S and visited[arr[i][1]] == 0:
                queue.append(arr[i][1])
                queue1.append(idx + 1)

            if arr[i][1] == S and visited[arr[i][0]] == 0:
                queue.append(arr[i][0])
                queue1.append(idx + 1)
        if G in queue:
            result = queue1[-1]
            break

    print('#{} {}'.format(tc, result))

