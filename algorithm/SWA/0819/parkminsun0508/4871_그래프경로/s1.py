# 4871 그래프 경로
# 다른 개념도 활용해 보기
import sys
sys.stdin = open("input.txt")


# DFS 함수 사용
def DFS(start):
    global result
    visited[start] =True
    for i in matrix[start]:
        if not visited[i]:
            # 도착노드와 같으면 1 반환
            if i == end:
                result = 1
                return
            DFS(i)

#테스트 케이스를 받아온다.
T = int(input())
for tc in range(1, T+1):
    # V => 노드, 정점
    # E => 엣지, 간선
    V, E = list(map(int, input().split()))
    matrix = [[] for _ in range(V + 1)]
    # 인접행렬
    for _ in range(E):
        start, end = map(int, input().split())
        matrix[start].append(end)
    # 시작, 도착 노드
    start, end = map(int, input().split())
    # 방문했는지 여부 체크 ( V = [ F F F F F F] )
    visited = [False] * (V+1)
    result = 0
    # 시작점 받기
    DFS(start)

    print("#{} {}".format(tc, result))




