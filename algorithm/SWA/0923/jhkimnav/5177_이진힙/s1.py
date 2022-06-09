import sys
sys.stdin = open('input.txt')


def binary_heap(idx):
    global tree
    while tree[idx//2] > tree[idx]:
        tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
        idx = idx // 2


T = int(input())
for TC in range(1, T+1):
    # 노드 개수
    N = int(input())
    node_list = list(map(int, input().split()))
    tree = [0]
    for i in range(N):
        tree.append(node_list[i])
        binary_heap(i+1)

    node = len(tree)-1
    sum_of_value = 0

    # 마지막 노드의 조상의 합 구하기
    while tree[node//2]:
        sum_of_value += tree[node//2]
        node = node // 2

    print('#{} {}'.format(TC, sum_of_value))

