import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # V: 노드 개수  E: 간선 개수
    V, E = map(int, input().split())
    # 간선 연결 정보
    con = [list(map(int, input().split())) for _ in range(E)]
    # S: 출발 노드  G: 도착 노드
    S, G = map(int, input().split())

    con_list = [[0]*(V+1) for _ in range(V+1)]

    for i in range(len(con)):
        con_list[con[i][0]][con[i][1]] = 1
        con_list[con[i][1]][con[i][0]] = 1

def bfs(s, g):
