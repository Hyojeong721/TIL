import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    total_list = []

    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += numbers[i+j]
        total_list.append(total)

    temp_max = total_list[0]
    temp_min = total_list[0]

    for k in total_list:

        if temp_max <= k:
            temp_max = k
        elif temp_min >= k:
            temp_min = k

    result = temp_max - temp_min

    print('#{} {}'.format(tc,result))



