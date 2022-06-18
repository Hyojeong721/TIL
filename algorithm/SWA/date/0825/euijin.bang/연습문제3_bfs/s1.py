import sys
sys.stdin = open("input.txt")

# V => 노드
# E => 엣지, 간선

V, E = map(int, input().split())
graph_list = list(map(int, input().split()))
print(graph_list)

# 인접행렬
graph = [[0 for _ in range(V+1)] for _ in range(V+1)] # 1과 인덱스를 통일
visited = [0 for _ in range(V+1)] # 한 번 방문한 곳은 다시 방문하지 않기 위해

for i in range(E): # 8개의 쌍을 돈다
    # 홀짝 분리
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1 # 무향그래프이므로 대칭 구조를 만듦

def bfs(v):
    queue = [v] # 1번 넣은 상태로 시작

    while len(queue): # 큐가 빌때까지 계속해서 작업한다
        v = queue.pop(0) # 맨 앞의 데이터를 뽑아 v 에 덮어씌운다 (위의 v와는 별개)
        if not visited[v]:    # 방문하지 않았다면
            visited[v] = 1
            print('{}번을 방문했습니다. {}'.format(v, visited))

            for w in range(1, V+1): # V 번째 노드까지 돌리면서 연결된 노드 찾음
                if graph[v][w] == 1 and visited[w] == 0: # v 행의 w 열이 1이면
                    queue.append(w)


bfs(1) # 1번 노드부터 시작

