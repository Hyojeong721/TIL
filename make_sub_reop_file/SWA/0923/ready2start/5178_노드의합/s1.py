import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # 마지막 노드가 왼쪽 노드인 경우에도
    # nodes[i] = nodes[i * 2] + nodes[i * 2 + 1]가 성립하도록
    # nodes에 한 칸의 여유를 둠.
    nodes = [0] * (N + 2)

    for _ in range(M):
        node, number = map(int, input().split())
        nodes[node] = number

    for i in range(N // 2, 0, -1):
        nodes[i] = nodes[i * 2] + nodes[i * 2 + 1]

    print("#{} {}".format(tc, nodes[L]))
