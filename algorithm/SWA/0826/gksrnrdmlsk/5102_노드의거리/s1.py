import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 개수, 간선 개수
    adj_lst = [[] for _ in range(V + 1)] # 인접 리스트를 구성합니다.
    lst = [list(map(int, input().split())) for _ in range(E)]
    for i in lst:
        adj_lst[i[0]].append(i[1])
        adj_lst[i[1]].append(i[0])
    S, G = map(int, input().split()) # 출발점과 도착점
    visited = [0] * (V + 1) # V개의 노드에 대한 거리를 구할 수 있는 빈 리스트
    Q = [S] # 큐 정의

    while Q: # BFS 탐색 시작
        curr = Q.pop(0) # 현재 탐색하는 노드
        for i in adj_lst[curr]:
                if visited[i] == 0:
                    visited[i] = visited[curr] + 1 # 깊어질수록 1씩 더하여 경로의 길이를 나타냄
                    Q.append(i) # 해당 노드를 큐에 추가합니다.

    print('#{} {}'.format(tc, visited[G])) # G에 대한 결과를 출력합니다.
