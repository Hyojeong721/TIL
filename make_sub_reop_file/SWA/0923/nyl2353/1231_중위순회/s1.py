import sys
sys.stdin = open('input.txt')

def inorder_traverse(v):
    """
    v를 root로 한 (sub)tree 에서 중위순회한 문자열을 result 에 업데이트한다.

    """
    global result

    if v <= N:
        inorder_traverse(2 * v)
        result += tree[v]
        inorder_traverse(2 * v + 1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        n, *v = input().split()
        tree[int(n)] = v[0]

    result = ''
    inorder_traverse(1)

    print('#{} {}'.format(tc, result))