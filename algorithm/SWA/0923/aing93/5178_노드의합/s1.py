import sys
sys.stdin = open('input.txt')

T = int(input())

for T in range(1, T+1):
    # M 리프 노드의 개수, L : 출력할 번호
    N, M, L = list(map(int, input().split()))
    # 짝수일때, 마지막노드 + 1 범위까지 검사하기 위해
    tree = [0] * (N+2)
    for _ in range(M):
        idx, value = list(map(int, input().split()))
        tree[idx] = value

    if N % 2 == 0:
        for i in range(N, 1, -2):
            tree[i//2] = tree[i] + tree[i+1]
    else:
        for j in range(N, 2, -2):
            tree[j//2] = tree[j] + tree[j-1]

    print('#{} {}'.format(T, tree[L]))