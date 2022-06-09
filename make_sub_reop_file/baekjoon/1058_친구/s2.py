import sys
sys.stdin = open('input.txt')

T= int(input())
nodes = [list(input()) for _ in range(T)]
visited = [[0 for _ in range(T)] for _ in range(T)]
print(nodes)
print(visited)
cnt = 0

for i in range(T):
    for j in range(T):
        for k in range(T):
            if j == k:
                continue
            if nodes[j][k] == 'Y' or (nodes[j][i] == 'Y' and nodes[i][k] == "Y"):
                visited[j][k] = 1
                print(i, j, k, visited)

print(visited)