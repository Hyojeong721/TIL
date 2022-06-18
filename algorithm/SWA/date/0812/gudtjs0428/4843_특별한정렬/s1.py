import sys
sys.stdin = open('input.txt')

def special_sort(nums):
    special_list = []
    i = 0
    while i < 10:
        if i % 2:
            min_num = min(nums)
            special_list.append(min_num)
            nums.remove(min_num)
        else:
            max_num = max(nums)
            special_list.append(max_num)
            nums.remove(max_num)
        i += 1

    return special_list

T = int(input())
for test_case in range(1, T + 1):
    input()
    nums = list(map(int, input().split()))
    print('#{}'.format(test_case), end=' ')
    for num in special_sort(nums):
        print(num, end=' ')
    print()