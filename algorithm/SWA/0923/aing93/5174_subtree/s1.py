import sys
sys.stdin = open('input.txt')

def my_preorder(n):
    global cnt

    if n:
        cnt += 1
        my_preorder(left[n])
        my_preorder(right[n])

    return cnt

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    node_nums = list(map(int, input().split()))
    V = E + 1
    cnt = 0

    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = node_nums[i*2], node_nums[i*2+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    result = my_preorder(N)
    print('#{} {}'.format(tc+1, result))