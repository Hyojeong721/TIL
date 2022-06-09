import sys
sys.stdin = open('input.txt')

def sort_nums(nums):
    sorted_nums = []
    for _ in range(nums.count('ZRO')):
        sorted_nums.append('ZRO')
    for _ in range(nums.count('ONE')):
        sorted_nums.append('ONE')
    for _ in range(nums.count('TWO')):
        sorted_nums.append('TWO')
    for _ in range(nums.count('THR')):
        sorted_nums.append('THR')
    for _ in range(nums.count('FOR')):
        sorted_nums.append('FOR')
    for _ in range(nums.count('FIV')):
        sorted_nums.append('FIV')
    for _ in range(nums.count('SIX')):
        sorted_nums.append('SIX')
    for _ in range(nums.count('SVN')):
        sorted_nums.append('SVN')
    for _ in range(nums.count('EGT')):
        sorted_nums.append('EGT')
    for _ in range(nums.count('NIN')):
        sorted_nums.append('NIN')

    return sorted_nums


T = int(input())
for tc in range(1, T + 1):
    input()
    nums = list(input().split())
    print('#{}'.format(tc))
    for num in sort_nums(nums):
        print(num, end=' ')
    print()
    print(len(sort_nums(nums)))