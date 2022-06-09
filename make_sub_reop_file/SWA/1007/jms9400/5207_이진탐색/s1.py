import sys
sys.stdin = open('input.txt')

T = int(input())

def binarysearch(l, r, a, k):

    m = (l + r)//2

    if arr1[m] == a:
        return 1

    if arr1[m] > a:
        if k == 2:
            return 0
        else:
            return binarysearch(l, m-1, a, 2)
    else:
        if k == 1:
            return 0
        else:
            return binarysearch(m+1, r, a, 1)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))
    cnt = 0

    for i in arr2:
        if binarysearch(0, N-1, i, 0) == 1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
