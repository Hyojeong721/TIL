import sys
sys.stdin = open('input.txt')


patterns = {
    '001101': '0',
    '010011': '1',
    '111011': '2',
    '110001': '3',
    '100011': '4',
    '110111': '5',
    '001011': '6',
    '111101': '7',
    '011001': '8',
    '101111': '9',
}

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
i = 0
while i <= len(bi_nums)-6:
    password = bi_nums[i: i+6]
    if password in patterns:
        result.append(patterns[password])
        i += 5
    i += 1
print(', '.join(result))

