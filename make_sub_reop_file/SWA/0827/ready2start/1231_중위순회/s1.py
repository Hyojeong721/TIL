import sys
sys.stdin = open("input.txt")


# 중위 순회하면서 값을 출력하는 함수
def inorder_traverse(node):
    if node:
        inorder_traverse(left[node])
        print(words[node], end="")
        inorder_traverse(right[node])


T = 10

for tc in range(1, T + 1):
    N = int(input())

    """
    words: 각 노드의 알파벳을 저장하는 배열
    left: 각 노드의 왼쪽 자식 노드를 저장하는 배열
    right: 각 노드의 오른쪽 자식 노드를 저장하는 배열
    """
    words = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        idx, char, *rest = input().split()
        words[int(idx)] = char

        # 현재 노드가 왼쪽 자식 노드를 가진다면
        if len(rest) >= 1:
            left[int(idx)] = int(rest[0])

        # 현재 노드가 오른쪽 자식 노드를 가진다면
        if len(rest) == 2:
            right[int(idx)] = int(rest[1])

    print("#{}".format(tc), end=" ")
    # 루트 노드에서부터 중위 순회를 진행한다.
    inorder_traverse(1)
    print()
