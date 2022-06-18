import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N+1)

    for i in range(1, N+1):
        tree[i] = numbers[i-1]
        if i > 1:
            if tree[i//2] > tree[i]:
                k = i
                while k != 1 and tree[k // 2] > tree[k]:
                    tree[k // 2], tree[k] = tree[k], tree[k // 2]
                    k = k // 2

    idx = N
    result = 0
    while idx:
        idx //= 2
        result += tree[idx]

    print('#{} {}'.format(test_case, result))

