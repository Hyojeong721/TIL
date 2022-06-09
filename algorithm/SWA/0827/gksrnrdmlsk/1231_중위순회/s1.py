import sys
sys.stdin = open('input.txt')

def inorder(n):
    global result
    if left[n]:
        inorder(left[n])
    result.append(nodes[n])
    if right[n]:
        inorder(right[n])

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = [[]] + [input().split() for _ in range(N)]
    nodes = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in lst:
        if len(i) == 2:
            nodes[int(i[0])] = i[1]
        elif len(i) == 4:
            nodes[int(i[0])] = i[1]
            left[int(i[0])] = int(i[2])
            right[int(i[0])] = int(i[3])
        elif len(i) == 3:
            nodes[int(i[0])] = i[1]
            left[int(i[0])] = int(i[2])

    result = []

    inorder(1)
    print('#{} {}'.format(tc, ''.join(result)))