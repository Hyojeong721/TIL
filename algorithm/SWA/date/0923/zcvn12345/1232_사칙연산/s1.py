import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        node = list(map(str, input().split()))
        tree[i] = node[1]


