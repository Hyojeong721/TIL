import sys
sys.stdin = open('input.txt')


def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1

    inorder(left[node])
    inorder(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))
    left = [0] + [0] * (E+1)
    right = [0] + [0] * (E+1)


    for i in range(0, len(tmp), 2):
        if not left[tmp[i]]:
            left[tmp[i]] = tmp[i+1]
        else:
            right[tmp[i]] = tmp[i + 1]


    cnt = 0
    inorder(N)

    print('#{} {}'.format(tc, cnt))


