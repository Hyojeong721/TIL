import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    Node = list(map(int, input().split()))
    tree = [0]*(2**20)
    cnt = 1
    for i in range(E):
        P = Node[2*i]
        C = Node[2*i+1]
        if P not in tree:
            tree[i+1] = P

        if tree[2*tree.index(P)] == 0:
            tree[2*tree.index(P)] = C
        else:
            tree[2*tree.index(P)+1] = C

    def search(num):
        global cnt
        if tree[2*tree.index(num)]:
            cnt += 1
            search(tree[2*tree.index(num)])

        if tree[2*tree.index(num)+1]:
            cnt += 1
            search(tree[2*tree.index(num)+1])

    search(N)
    print(f'#{tc} {cnt}')



