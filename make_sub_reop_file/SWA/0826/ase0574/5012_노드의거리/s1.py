# 7/10개 통과 코드

import sys
sys.stdin = open('input.txt')
# 주어진 출발 노드에서
# 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램
T = int(input())

def bfs(S, G):
    queue = [S]

    while len(queue):
        front = queue.pop(0)
            ### 여기가 문제점!! ###
        if not visited[front]:
            visited[front] = 1
            ######################

            # 이어진 노드들 찾기
            for j in range(V+1):
                if graph[front][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    # 간선 저장
                    result[j] = result[front] + 1

    if result[G]:
        print("#{} {}".format(tc, result[G]))
    else:
        print("#{} 0".format(tc))


for tc in range(1, T+1):
    # V개의 노드 개수와 방향성이 없는 E개의 간선 정보
    V, E = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(E)]

    # 출발 노드 S와 도착 노드 G
    S, G = list(map(int, input().split()))

    # 간선 그래프 그리기
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        start = data[i][0]
        end = data[i][1]

        graph[start][end] = 1
        graph[end][start] = 1

    visited = [0 for _ in range(V+1)]
    result = [0 for _ in range(V+1)]
    bfs(S, G)

