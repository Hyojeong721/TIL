import sys
sys.stdin = open('input.txt')


def preorder_traverse(node, order):
    """
    주어진 트리를 전위 순회한다.
    (왼쪽 서브트리 - 루트 노드 - 오른쪽 서브트리 순)
    """
    if not node:
        return

    preorder_traverse(left[node], order)
    order.append(node)
    preorder_traverse(right[node], order)

    return order


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # left: 왼쪽 자식 노드
    # right: 오른쪽 자식 노드
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 노드가 N개인 완전 이진 트리를 만든다.
    for i in range(2, N + 1):
        if i % 2 == 0:
            left[i // 2] = i
        else:
            right[i // 2] = i

    # order: 노드가 N개인 완전 이진 트리를 전위 순회하는 순서
    order = preorder_traverse(1, [])
    print("#{} {} {}".format(tc, order.index(1) + 1, order.index(N // 2) + 1))
