import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    tree = [0]

    for idx, node in enumerate(nodes, 1):
        tree.append(node)

        while node < tree[idx // 2]:
            tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
            idx //= 2


    total = 0
    tmp = len(nodes)
    while tmp > 1:
        tmp //= 2
        print(tmp)
        total += tree[tmp]

    print('#{} {}'.format(tc, total))