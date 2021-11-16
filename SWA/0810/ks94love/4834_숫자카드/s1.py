import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    result_list = [0] * 10
    numbers = input()

    for number in numbers:
        result_list[int(number)] += 1

    max_num = result_list[0]
    max_idx = 0

    for idx, num in enumerate(result_list):
        if num >= max_num:
            max_num = num
            max_idx = idx

    print('#{} {} {}'.format(i+1, max_idx, max_num))