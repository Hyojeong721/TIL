import sys

sys.stdin = open('input.txt')

T = 10

for TC in range(1, T + 1):
    dump = int(input())
    box_list = list(map(int, input().split()))
    #print(box_list)

    while dump > 0:
        max_value = box_list[0]
        max_idx = 0
        min_value = box_list[0]
        min_idx = 0
        for idx, value in enumerate(box_list):


            if value > max_value:
                max_value = value
                max_idx = idx
            elif value < min_value:
                min_value = value
                min_idx = idx

        box_list[max_idx] -= 1
        box_list[min_idx] += 1
        dump -= 1
        max_value = box_list[0]
        max_idx = 0
        min_value = box_list[0]
        min_idx = 0

        for idx, value in enumerate(box_list):

            if value > max_value:
                max_value = value
                max_idx = idx
            elif value < min_value:
                min_value = value
                min_idx = idx
        # print(max_idx, max_value, min_idx, min_value)

    print('#{0} {1}'.format(TC, max_value-min_value))
