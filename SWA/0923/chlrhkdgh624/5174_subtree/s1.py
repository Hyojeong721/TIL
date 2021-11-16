import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # E, N
    E, N = map(int, input().split())
    nodes = [[0] * (E+2) for _ in range(E+2)]
    edges = list(map(int, input().split()))
    # 부모-자식 연결 상태 입력 -> (부모,자식)
    for i in range(E):
        parent = edges[2*i]
        child = edges[2*i+1]
        nodes[parent][child] = 1

    stack = [N]
    num = 1

    while stack:
        parent = stack.pop()
        for child in range(E+2):
            if nodes[parent][child] == 1:
                num += 1
                stack.append(child)

    print(f'#{tc} {num}')
