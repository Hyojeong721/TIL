import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    x_list = [0] * 100
    y_list = [0] * 100
    z_list = [0, 0]
    tc = input()
    for i in range(100):
        num_list = list(map(int, input().split()))

        for j in range(100):
            x_list[i] += num_list[j]
            y_list[j] += num_list[j]
            if i == j:
                z_list[0] += num_list[j]
            if i + j == 99:
                z_list[1] += num_list[j]

    max_num = 0

    for i in range(100):
        if x_list[i] > max_num:
            max_num = x_list[i]
        if y_list[i] > max_num:
            max_num = y_list[i]

    for value in z_list:
        if value > max_num:
            max_num = value

    print(max_num)