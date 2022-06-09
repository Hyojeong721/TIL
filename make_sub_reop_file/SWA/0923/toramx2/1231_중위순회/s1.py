import sys
sys.stdin = open('input.txt')

def inorder(a):
    if a <= N:
        inorder(a*2)
        print(tree[a], end='')
        inorder(a*2+1)

T = 10

for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(N):
        line = list(input().split())
        tree[i+1] = line[1]

    print('#{}'.format(test_case), end=' ')
    inorder(1)
    print()
