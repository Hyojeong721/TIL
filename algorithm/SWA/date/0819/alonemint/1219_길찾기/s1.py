import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 1 + T):
    Q_num, N = map(int, input().split())

    #init block
    stack = [0]
    checked = [0] * 100
    adj = [[0] * 100 for _ in range(100)]
    E = list(map(int, input().split()))
    for i in range(N):
        n1, n2 = E[2 * i], E[2 * i + 1]
        adj[n1][n2] = 1

    #dfs block
    while stack:
        v = stack.pop()
        if not checked[v]:
            checked[v] = 1

        for w in range(100):
            if adj[v][w] == 1 and checked[w] == 0:
                stack.append(w)

    #final block
    if checked[99]:
        print('#{} {}'.format(Q_num, 1))
    else:
        print('#{} {}'.format(Q_num, 0))