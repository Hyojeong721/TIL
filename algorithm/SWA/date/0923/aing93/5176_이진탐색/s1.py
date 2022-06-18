import sys
sys.stdin = open('input.txt')


def MakeTree(node):
    global cnt

    if node <= N:
        MakeTree(node*2) # 왼쪽노드

        tree[node] = cnt # 중간(부모)노드
        cnt += 1

        MakeTree(node*2+1) # 오른쪽 노드

    else:
        return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    MakeTree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))