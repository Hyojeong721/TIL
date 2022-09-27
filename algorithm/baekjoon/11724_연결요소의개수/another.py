import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])

    return parents[a]


def union(a, b):
    if parents[a] == parents[b]:
        return
    a_root = find(a)
    b_root = find(b)

    if a_root > b_root:
        parents[a] = b_root
    else:
        parents[b] = a_root

for _ in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)


for k in range(n):
    find(k)

print(len(set(parents)))