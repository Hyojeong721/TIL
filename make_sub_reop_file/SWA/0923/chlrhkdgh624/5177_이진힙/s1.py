import sys
sys.stdin = open('input.txt')
T = int(input())


def find_ancestor(x):
    ancestors = []
    while x > 1:
        x //= 2
        ancestors.append(x)
    return ancestors


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [None, numbers[0]]
    for i in range(1, N):
        new_num = numbers[i]
        tree.append(new_num)
        check_list = find_ancestor(tree.index(new_num))
        for j in check_list:
            x = tree.index(new_num)
            if tree[j] > new_num:
                tree[j], tree[x] = tree[x], tree[j]

    result = find_ancestor(N)
    result = list(map(lambda x: tree[x], result))
    print(f'#{tc} {sum(result)}')




