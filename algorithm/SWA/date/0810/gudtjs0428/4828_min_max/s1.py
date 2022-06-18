import sys
sys.stdin = open('input.txt')

T = int(input())

def get_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

def get_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def dif(nums):
    return get_max(nums) - get_min(nums)


for tc in range(1, T + 1):
    input()
    nums = list(map(int, input().split()))
    print('#{0} {1}'.format(tc, dif(nums)))