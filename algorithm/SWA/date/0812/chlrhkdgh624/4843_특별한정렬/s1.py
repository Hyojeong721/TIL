import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    num_list = list(map(int, input().split()))
    ascending_list = num_list[:]

    for i in range(N, 0, -1):
        for j in range(0, i-1):
            if ascending_list[j] > ascending_list[j+1]:
                ascending_list[j], ascending_list[j + 1] = ascending_list[j+1], ascending_list[j]

    descending_list = [ascending_list[x] for x in range(N-1, -1, -1)]

    special_sort = []
    for k in range(N):
        special_sort.append(descending_list[k])
        special_sort.append(ascending_list[k])

    result = ' '.join(map(str, special_sort[:10]))

    print(f'#{tc} {result}')
