import sys
sys.stdin = open('input.txt')


def bfs(v):
    visit[v] = 1
    que = [v]

    while que:
        v = que.pop(0)

        # pop한 노드가 도착점일 경우 반복 종료
        if v == G:
            result = visit[v] - 1
            return result

        if v in arr.keys():     # key값 존재  여부 확인
            for w in arr.get(v):    # 해당 key의 value들 확인
                if not visit[w]:    # 방문하지 않은 경우
                    visit[w] = visit[v] + 1 # 현재노드까지의 거리 + 1
                    que.append(w)

    # 반복중 도착점 못 찾은 경우 0 반환
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(S,G)

    # 노드 딕셔너리 생성
    ## {현재 노드: [연결된 노드], ...}
    arr = {}
    for m in mat:
        node1 = m[0]
        node2 = m[1]
        arr[node1] = arr.get(node1, []) + [node2]
        arr[node2] = arr.get(node2, []) + [node1]
    # print(arr)

    # 시작점으로부터의 거리를 저장할 리스트
    visit = [0] * (V + 1)

    ans = bfs(S)
    print('#{} {}'.format(tc, ans))
