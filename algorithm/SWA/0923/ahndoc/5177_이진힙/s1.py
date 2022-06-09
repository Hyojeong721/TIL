import sys
sys.stdin = open('input.txt')

def heap(n):
    if n // 2 < 0:
        return
    else:
        if tree[n // 2] > tree[n]:
            tree[n // 2], tree[n] = tree[n], tree[n // 2]
            heap(n // 2)
# def heap(node):
#     mom_node = node//2
#     if mom_node < 0:
#         return
#     else:
#         if tree[mom_node] > tree[node]:
#             tree[node], tree[mom_node] = tree[mom_node], tree[node]
#             heap(mom_node)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0]

    v = 1
    for number in arr:
        tree.append(number)
        heap(v)
        v += 1
    sum_v = 0
    while N > 1:
        sum_v += tree[N // 2]
        N //= 2
    print('#{} {}'.format(tc, sum_v))


