import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(S,G)

    arr = {}
    for m in mat:
        node1 = m[0]
        node2 = m[1]
        arr[node1] = arr.get(node1, []) + [node2]
        arr[node2] = arr.get(node2, []) + [node1]
    print(arr)

    visit = [0] * (V + 1)

    def bfs(v):
        result = 0
        visit[v] = 1
        que = [v]

        while que:
            v = que.pop(0)

            if v in arr.keys():     # key값 존재  여부 확인
                for w in arr.get(v):    # 해당 key의 value들 확인
                    if not visit[w]:
                        visit[w] = visit[v] + 1
                        que.append(w)

                        if w == G:
                            result = visit[w] - 1
                            return result
        return result

    ans = bfs(S)

    print('#{} {}'.format(tc, ans))
