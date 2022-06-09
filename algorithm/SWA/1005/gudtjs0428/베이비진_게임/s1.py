import sys
sys.stdin = open('sample_input.txt')


def if_babygin(num_count):
    for j in range(10):
        if num_count[j] >= 3:
            return 1
        if j <= 7 and num_count[j] >= 1 and num_count[j + 1] >= 1 and num_count[j + 2] >= 1:
            return 1


T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    p1, p2 = [0] * 10, [0] * 10
    draw = 1
    for i in range(12):
        if i % 2:
            p2[nums[i]] += 1
        else:
            p1[nums[i]] += 1
        if i >= 5:
            if if_babygin(p1):
                print('#{} 1'.format(test_case))
                draw = 0
                break
            if if_babygin(p2):
                print('#{} 2'.format(test_case))
                draw = 0
                break
    if draw:
        print('#{} 0'.format(test_case))

