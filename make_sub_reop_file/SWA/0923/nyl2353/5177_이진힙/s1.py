import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0]

    for idx, number in enumerate(numbers, 1):
        tree.append(number)
        while idx:
            if tree[idx] <= tree[idx//2]:
                tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
            idx //= 2

    ans = 0
    p = N // 2
    while p:
        ans += tree[p]
        p //= 2

    print('#{} {}'.format(tc, ans))