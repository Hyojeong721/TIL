import sys
sys.stdin = open('input.txt')


def inorder_traverse(node):
    """
    주어진 노드를 루트 노드로 하는 트리를 중위 순회한다.
    (왼쪽 자식 트리 - 루트 노드 - 오른쪽 자식 트리)
    """
    if left[node]:
        inorder_traverse(left[node])

    print(words[node], end="")

    if right[node]:
        inorder_traverse(right[node])


T = 10

for tc in range(1, T + 1):
    N = int(input())

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    words = [""]

    for _ in range(N):
        node, word, *child = input().split()
        words.append(word)

        # node의 왼쪽 자식이 있다면
        if child:
            left[int(node)] = int(child[0])
        # node의 오른쪽 자식이 있다면
        if len(child) == 2:
            right[int(node)] = int(child[1])

    print("#{}".format(tc), end=" ")
    inorder_traverse(1)
    print()
