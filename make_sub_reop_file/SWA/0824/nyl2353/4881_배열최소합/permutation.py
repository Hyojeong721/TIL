def permutation(k):
    global visited

    if k == N:
        print(visited)

    for idx in range(k, N):
        visited[k], visited[idx] = visited[idx], visited[k]
        permutation(k + 1)
        visited[k], visited[idx] = visited[idx], visited[k]


N = 3
visited = [0] * N
for i in range(N):
    visited[i] = i

permutation(0)