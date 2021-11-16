import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    # 버스 노선 수
    N = int(input()) # 2

    graph = [0]*5001

    # 노선 정보
    for i in range(N):
        A, B = map(int, input().split()) # 1 3   # 2 5
        # 그래프에 버스 정류장 지나는 거 전부 1로 체크
        for j in range(A, B+1):  # 1. 2. 3   # 2, 3, 4, 5
            graph[j] += 1

    # 버스 정류장 수
    P = int(input()) # 5
    # 버스 정류장을 지나가는 노선 수 출력
    for i in range(P):
        station = int(input())
        print(graph[station], end=' ')
    # 프린트 한번 더 안찍으면 tc가 두 개일때도 계속 한줄로 출력됨
    print()