import sys
sys.stdin = open('input.txt')

def rotate(nums, M):
    pass
    i = M
    while i > 0:
        nums.append(nums.pop(0))
        i -= 1
    return nums[0]

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(test_case, rotate(nums, M)))