import sys
sys.stdin = open('input.txt')

def bst(i):
    global v
    if i <= N:
        bst(i*2)
        tree[i] = v
        v += 1
        bst(i*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)
    v = 1
    bst(v)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))