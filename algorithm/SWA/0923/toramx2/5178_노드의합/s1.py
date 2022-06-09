import sys
sys.stdin = open('input.txt')

def find_node(a):
    if tree[a] == 0:
        try:
            tree[a] = tree[a*2] + tree[a*2+1]
        except:
            tree[a] = tree[a*2]
    return


T = int(input())

for test_case in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    tree = [0] * (N+1)
    for _ in range(M):
        node, number = list(map(int, input().split()))
        tree[node] = number

    for i in range(N, 0, -1):
        find_node(i)

    print('#{} {}'.format(test_case, tree[L]))