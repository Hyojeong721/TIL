import sys
sys.stdin = open("input.txt")


V, E = map(int, input().split())
# 연결된 두 정점의 목록이 나열되어 있다.
graph = [int(x) for x in input().split()]

# adj_list: 인접 리스트
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    start, end = graph[i * 2], graph[i * 2 + 1]
    # 무방향 그래프이므로 양쪽에 모두 표시한다.
    adj_list[start].append(end)
    adj_list[end].append(start)

visited = [False] * (V + 1)


def bfs(v):
    queue = [v]
    visited[v] = True

    while queue:
        cnt = queue.pop(0)
        print("{}을 방문했습니다.".format(cnt))

        for node in adj_list[cnt]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

bfs(1)
