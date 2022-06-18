import sys
sys.stdin = open('input.txt')

def dfs(s, g):
    global adj
    visited = [0] * 100
    stack = [s]

    while len(stack):
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            for w in range(100):
                if adj[v][w] and visited[w] == 0:
                    stack.append(w)
    if visited[g]:
        return 1
    return 0


T = 10
for tc in range(1, T+1):
    tc, N = list(map(int, input().split()))
    data = list(map(int, input().split()))

    # 1. ch1, ch2
    # ch1 = [0] * 100
    # ch2 = [0] * 100
    # for i in range(N):
    #     if ch1[data[2*i]] == 0:
    #         ch1[data[2*i]] = data[2*i+1]]
    #     else:
    #         ch2[data[2*i]] = data[2*i+1]

    # 2. 인접 행렬 방식
    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(len(data)//2):
        adj_arr[data[i*2]][data[i*2+1]] = 1

    print('#{} {}'.format(tc, dfs(0, 99)))

    # 3. 인접 리스트 방식
    # adj_list = [[] for _ in range(N)]
    # for i in range(N):
    #     adj_list[data[2*i]].append(data[2*i+1])




