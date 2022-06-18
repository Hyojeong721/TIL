import sys
sys.stdin = open("input.txt")


# 전위 순회하면서 값을 출력하는 함수
def preorder_traverse(node):
    if node:
        print(node, end=" ")
        preorder_traverse(left_nodes[node])
        preorder_traverse(right_nodes[node])


N = int(input())
edges = [int(x) for x in input().split()]

# left_nodes: 각 노드의 왼쪽 자식 노드를 저장하는 배열
# right_nodes: 각 노드의 오른쪽 자식 노드를 저장하는 배열
left_nodes = [0] * (N + 1)
right_nodes = [0] * (N + 1)

for i in range(len(edges) // 2):
    a, b = edges[i * 2], edges[i * 2 + 1]
    # 왼쪽 자식 노드가 이미 있다면 => 오른쪽 자식 노드로 추가
    if left_nodes[a]:
        right_nodes[a] = b
    # 왼쪽 자식 노드가 없다면 => 왼쪽 자식 노드로 추가
    else:
        left_nodes[a] = b

# 루트 노드에서부터 전위 순회를 진행한다.
preorder_traverse(edges[0])
