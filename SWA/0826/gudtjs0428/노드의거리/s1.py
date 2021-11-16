import sys
sys.stdin = open('input.txt')

def get_distance(graph, now, end, visitied, count, E):
    global min_count
    if count < min_count:
        for to_visit in graph[now]:
            if not visited[to_visit]:
                count += 1
                if to_visit == end and count < min_count:
                    min_count = count
                    return
                visited[to_visit] = 1
                now = to_visit
                get_distance(graph, now, end, visitied, count, E)
    if min_count == E + 1:
        return 0
    else:
        return min_count

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        route = list(map(int, input().split()))
        graph[route[0]].append(route[1])
        graph[route[1]].append(route[0])
    start, end = map(int, input().split())
    visited = [0] * (V + 1)
    visited[start] = 1
    count = 0
    min_count = E + 1
    print('#{} {}'.format(test_case, get_distance(graph, start, end, visited, count, E)))