import sys
sys.stdin = open('input.txt')

#V는 노드 / E는 간선
V, E = list(map(int, input().split()))

#연결 정점 정보
graph_list = list(map(int, input().split()))


#V+1 -> 노드 0 은 없지만 인덱스 접근할 때 숫자 편하게 하려고!
graph = [[0 for _ in range(V+1)]for _ in range(V+1)]
#방문 기록용 리스트
visited = [0 for _ in range(V+1)]

for i in range(E):
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1

#v는 시작하는 노드
def dfs(v):
    global graph, visited, V

    stack =[v]
    # 스택이 비어있지 않으면 계속 DFS 진행
    while len(stack):
        #가장 마지막에 넣었던 위치를 빼온다.
        v = stack.pop()

        #마지막 위치가 방문하지 않은 곳이라면
        if visited[v] == 0:
            # 방문 기록!
            visited[v] = 1
            print('방문한 위치{} visited{}'.format(v, visited))

            for w in range(1, V+1):
                if graph[v][w] == 0 and visited[w] ==0:
                    stack.append(w)

dfs(1)





