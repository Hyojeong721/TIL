import sys
sys.stdin = open('input.txt')
T = int(input())


def binary_search(x):
    global cnt
    if x <= N:
        binary_search(2*x)
        tree[x] = cnt
        cnt += 1
        binary_search(2*x+1)

    return tree



for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    cnt = 1
    binary_search(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')

