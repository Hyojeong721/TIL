
import sys
sys.stdin = open('input.txt')

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y]:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    else:
        parent[x] = y


def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])


T = int(input())
for test_case in range(1, 1+ T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for i in range(M):
        union(data[2 * i], data[2 * i + 1])
    groups = set()

    for j in range(1, 1 + N):
        groups.add(find_set(j))
    print(rank)
    print('#{} {}'.format(test_case, len(groups)))