import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nodes = [int(x) for x in input().split()]

    # tree: 완전 이진 트리 (배열의 n번째 인덱스의 값 = 트리의 n번째 노드의 값)
    tree = [0]

    for idx, node in enumerate(nodes, 1):
        tree.append(node)
        # 현재 추가한 노드가 부모 노드보다 작다면, 위치를 바꿔준다.
        while node < tree[idx // 2]:
            tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
            idx //= 2

    # total: 마지막 노드의 조상 노드에 저장된 정수의 합
    total, cnt_idx = 0, len(nodes)

    while cnt_idx:
        total += tree[cnt_idx // 2]
        cnt_idx //= 2

    print("#{} {}".format(tc, total))