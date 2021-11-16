import sys
sys.stdin = open("input.txt", "r")

def get_max(my_list):
    max_value = my_list[0]
    for lis in my_list:
        if max_value < lis:
            max_value = lis
    return max_value

TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    build = list(map(int, input().split()))

    # result = 0
    # for i in range(2, N-2):
    #     # build_list = [build[i-2], build[i-1], build[i+1], build[i+2]]
    #     #
    #     # max_build = build[i-2]
    #     # for j in range(len(build_list)):
    #     #     if max_build < build_list[j]:
    #     #         max_build = build_list[j]
    #     max_build = get_max([build[i-2], build[i-1], build[i+1], build[i+2]])
    #
    #     if build[i] > max_build:
    #         result += build[i] - max_build
    #
    # print('#{} {}'.format(tc, result))
    total = 0
    for i in range(2, N-2):
        temp = []
        for j in range(2):
            temp.append(build[i+j+1])
            temp.append(build[i-j-1])
        result = 0
        t = build[i]
        max_v = temp[0]
        for k in temp:
            if max_v < k:
                max_v = k

        if max_v < t:
            result = t - max_v
        total += result

    print('#{} {}'.format(tc, total))



