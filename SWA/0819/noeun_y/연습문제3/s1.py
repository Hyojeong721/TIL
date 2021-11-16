
import sys
sys.stdin = open('input.txt')

V,E = list(map(int,input().split()))

graph_list = list(map(int,input().split()))

graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

visited=[0 for _ in range(V+1)]
for i in range(0,len(graph_list),2):

    start = graph_list[i]
    end = graph_list[i+1]

    graph[start][end]=1
    graph[end][start]=1

def dfs(v):
    global graph,visited, V
    stack = [v]

    while len(stack):
        v= stack.pop()

        if visited[v]==0:
            visited[v]=1
            print('방문한 위치 {} visited{}'.format(v,visited))


            for w in range(1,V+1):
                if graph[v][w]==1 and visited[w] ==0:
                    stack.append(w)


dfs(1)





