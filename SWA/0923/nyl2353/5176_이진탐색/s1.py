import sys
sys.stdin = open('input.txt')

def make_tree(node):
    global cnt

    if node <= N:
        make_tree(node*2)

        tree[node] = cnt
        cnt += 1

        make_tree(node*2 + 1)

    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)

    cnt = 1
    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
