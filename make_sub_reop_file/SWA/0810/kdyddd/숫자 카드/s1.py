import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    a = input()
    b = list(map(int, list(input())))
    num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in b:
        num_list[i] += 1

    max_num = 0
    num = 0

    for i in range(0, 10):
        if num_list[i] >= max_num:
            max_num = num_list[i]
            num = i

    print(f'#{test_case} {num} {max_num}')
