import sys
sys.stdin = open('input.txt')

def inorder(i):
    if i <= N:
        inorder(i*2)
        ans.append(tree[i])
        inorder(i*2+1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    # print(arr)
    tree = [0 for _ in range(N+1)]
    # print(tree)
    for i in range(N):
        tree[int(arr[i][0])] = arr[i][1]
    # print(tree)
    ans = []
    inorder(1)
    result = ''
    for alp in ans:
        result += alp

    print('#{} {}'.format(tc, result))



        # for n in node:
        #     if n.isdigit():
        #         if left[int(n)]:
        #             pass
        #         else:
        #             left[int(n)] =
