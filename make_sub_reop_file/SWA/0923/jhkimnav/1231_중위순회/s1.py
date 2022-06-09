import sys
sys.stdin = open("input.txt", "r")


def in_order(n):
    if n <= N:
        in_order(n*2)
        print(tree[n], end='')
        in_order(n*2+1)

T = 10
for TC in range(1, T+1):
    N = int(input())
    tree = ['0'] * (N + 1)
    for _ in range(N):
        input_data = list(input().split())
        idx = int(input_data[0])
        tree[idx] = input_data[1]
    print('#{} '.format(TC), end='')
    in_order(1)
    print()
