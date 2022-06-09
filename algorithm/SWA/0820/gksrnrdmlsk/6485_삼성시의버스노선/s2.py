import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = [0] * 5001
    start_lst = [0] * 5001
    end_lst = [0]* 5001
    N = int(input())
    for _ in range(N):
        i, j = map(int, input().split())
        start_lst[i] += 1
        end_lst[j] += 1

    cnt = 0
    for k in range(1, 5001):
        cnt += start_lst[k]
        cnt -= end_lst[k - 1]
        lst[k] = cnt

    P = int(input())
    stops = [int(input()) for _ in range(P)]
    result = ' '.join(map(str, [lst[i] for i in stops]))
    print('#{} {}'.format(tc, result))