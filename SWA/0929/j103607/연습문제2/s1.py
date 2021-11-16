import sys
sys.stdin = open('input.txt')

'''
bin() : int값을 2진수 문자열로 반환
'''

nums = input()

bi_nums = ''
for i in nums:
    bi_single = bin(int(i, 16))
    if len(bi_single[2:]) != 4:
        bi_single = '0'*(4-len(bi_single[2:])) + bi_single[2:]
    else:
        bi_single = bi_single[2:]
    bi_nums += bi_single

result = []
for i in range(len(bi_nums)//7):
    bi_single = int(bi_nums[7*i: 7*i+7], 2)
    result.append(str(bi_single))

print(", ".join(result))

