import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())
    lst = list(map(int, input().split()))
    total = [0] * 12
    temp = 0

    total[0] = min(M, lst[0] * D)
    total[1] = total[0] + min(M, lst[1] * D)

    for i in range(2, 12):
        total[i] = min(total[i-3] + M3, total[i-1] + M, total[i-1] + lst[i] * D)
    print(min(total[-1], Y))

    # for i in range(len(lst)):
    #     if lst[i] != 0:
    #         temp += 1
    #         if lst[i] * D < M:
    #             total[i] = lst[i] * D
    #         else:
    #             total[i] = M
    #
    # j = 2
    # while j < 12:
    #     if total[j] + total[j-1] + total[j-2] > M3:
    #         total[j], total[j-1] = 0, 0
    #         total[j-2] = M3
    #         j += 2
    #     j += 1
    #
    # answer = sum(total)
    #
    # if answer > Y:
    #     answer = Y
    #
    # print('#{} {}'.format(tc, answer))

    # 47개맞음
