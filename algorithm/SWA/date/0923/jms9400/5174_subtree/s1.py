import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())  # N 루트로 하는 서브트리 속한 노드의 개수
    tre = list(map(int, input().split()))
    tree = list([] for _ in range(E+2))

    for i in range(len(tre)):
        if i % 2 == 0:
            a = tre[i]
        else:
            tree[a].append(tre[i])

    answer = 1
    temp = []
    if len(tree[N]) != 0:
        temp += tree[N]
        while len(temp):
            answer += 1
            b = temp.pop(0)
            if len(tree[b]) != 0:
                temp += tree[b]

    print('#{} {}'.format(tc, answer))
