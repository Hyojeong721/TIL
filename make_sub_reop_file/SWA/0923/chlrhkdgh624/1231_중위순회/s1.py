import sys
sys.stdin = open('input.txt')


def inorder_traversal(n):
    global result
    if n < N+1:
        inorder_traversal(2*n)
        result += tree[n]
        inorder_traversal(2*n+1)

    return result


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)

    for _ in range(N):
        test_input = input().split()
        test_input.reverse()
        node = int(test_input.pop(-1))
        tree[node] = test_input.pop()

    result = ''
    word = inorder_traversal(1)
    print(f'#{tc} {word}')


