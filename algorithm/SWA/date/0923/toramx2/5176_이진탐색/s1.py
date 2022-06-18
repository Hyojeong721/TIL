import sys
sys.stdin = open('input.txt')

def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)
        tree[n] = cnt
        cnt += 1
        inorder(n*2+1)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cnt = 1
    tree = [0 for _ in range(N+1)]
    inorder(1)
    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))