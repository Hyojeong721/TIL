import sys
sys.stdin = open('input.txt')
# 몇개의 무리가 존재하는지
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        pass
    else:
        parent[y] = x



def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)

    for i in range(M):
        union(data[i][0], data[i][1])

    for k in range(1, N+1):
        parent[k] = find(k)

    group = set()

    for j in range(1, N+1):
        group.add(parent[j])

    print("#{} {}".format(tc, len(group)))