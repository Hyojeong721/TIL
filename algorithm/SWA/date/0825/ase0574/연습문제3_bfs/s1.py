import sys
sys.stdin = open('input.txt')
# N = 노드 / V = 간선
V, E = list(map(int, input().split()))
graph_list = list(map(int, input().split()))
# 연결점들을 작성할 그래프
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
# 방문기록 리스트  /  V+1 -> 인덱스 번호 그대로 사용하려고!
visited = [0 for _ in range(V+1)]

# 이어진 점들 그래프에 작성!!!!
for i in range(E):
    start = graph_list[i * 2]
    end = graph_list[i * 2 + 1]

    graph[start][end] = 1
    graph[end][start] = 1

def bfs(f):
    queue = [f]     # queue에서 맨 첫번째꺼 빼온다.

    while queue:
        f = queue.pop(0)
        if visited[f] != 1:             # 방문한 적 없는 점이라면
            visited[f] = 1              # s점에 방문기록을 남긴다.
            print('{}방문함'.format(f))

        # 연결된 점들을 불러온다.
        for i in range(V+1):
            # 연결된 점들이 방문한적 없는 점들이라면 queue에 남긴다.
            if graph[f][i] == 1 and visited[i] == 0:
                queue.append(i)

bfs(1)