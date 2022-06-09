import sys
sys.stdin = open('input.txt')


def count_node(node):
    """
    주어진 노드를 루트로 하는 트리의 노드 개수를 구한다.
    (루트 노드 + 왼쪽 서브트리의 노드 개수 + 오른쪽 서브트리의 노드 개수)
    """
    if not node:
        return 0

    return 1 + count_node(left[node]) + count_node(right[node])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = [int(x) for x in input().split()]

    # left: 왼쪽 자식 노드
    # right: 오른쪽 자식 노드
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for idx in range(E):
        parent, child = nodes[2 * idx], nodes[2 * idx + 1]

        # 왼쪽 노드가 이미 있는 경우 => 오른쪽 노드에 추가
        if left[parent]:
            right[parent] = child
        # 왼쪽 노드가 빈 경우 => 왼쪽 노드에 추가
        else:
            left[parent] = child

    count = count_node(N)
    print("#{} {}".format(tc, count))
