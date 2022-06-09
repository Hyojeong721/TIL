import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M_list = arr[1:] + [0]

    cnt = 0

    i = 0
    gas = M_list[0]
    max_gas = 0
    max_i = 0

    while i < N-1:
        if i + gas > N-1:
            break
        for j in range(1, gas+1):
            if j+i < N-1 and M_list[j+i] >= max_gas:
                max_gas = M_list[j+i]
                # 0  1
                # 2 (3) 1 1

                max_i = j+i
        gas -= max_i - i
        i = max_i
        gas = max_gas
        max_gas = 0
        cnt += 1

    print('#{} {}'.format(tc, cnt))
