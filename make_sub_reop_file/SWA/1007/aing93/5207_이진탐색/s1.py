import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0

    for i in range(m):
        lt = 0
        rt = n-1
        target = b[i]
        history = 0
        while lt <= rt:
            mid = (lt+rt) // 2
            if target == a[mid]:
                cnt += 1
                break
            elif target > a[mid]:
                if history == 2:
                    break
                else:
                    lt = mid + 1
                    history = 2
            elif target < a[mid]:
                if history == 1:
                    break
                else:
                    rt = mid - 1
                    history = 1
    print('#{} {}'.format(tc, cnt))


