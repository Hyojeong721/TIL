import sys
sys.stdin = open('input.txt')

# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
# 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.

def mst(v):
    key[v]=0
    for _ in range(V):
        minindex=-1
        min = INF
        for i in range(V):
            if not visited[i] and key[i] < min:
                min = key[i]
                minindex = i
            visited[minindex] = 1
            for j in range(E):
                if data[j][0] == minindex:
                    v = data[j][1]
                    val = data[j][2]
                    if not visited[v] and val < key[v]:
                        key[v] = val
                        pi[v] = minindex


    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    pi = [-1] * V # 부모
    key = [INF] * V # 가중치
    visited = [0] * V # 방문기록
    print(data)

    mst(0)
