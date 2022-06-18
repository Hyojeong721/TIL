import sys
sys.stdin = open('input.txt')


def in_order(n):
    global N
    global value

    if n <= N:
        in_order(n*2)

        tree[n] = value
        value += 1

        in_order(n*2+1)


T = int(input())

for T in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    value = 1

    in_order(1)
    root = tree[1]
    print('#{} {} {}'.format(T, root, tree[N//2]))