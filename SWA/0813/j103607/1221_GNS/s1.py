import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    case_list = list(input().split())
    case_number = case_list[0] # #1(str)
    case_length = int(case_list[1]) # 7041(int)

    str_num = list(input().split())

    result = []
    for num in str_num:
        if num == 'ZRO':
            result.append('ZRO')
    for num in str_num:
        if num == 'ONE':
            result.append('ONE')
    for num in str_num:
        if num == 'TWO':
            result.append('TWO')
    for num in str_num:
        if num == 'THR':
            result.append('THR')
    for num in str_num:
        if num == 'FOR':
            result.append('FOR')
    for num in str_num:
        if num == 'FIV':
            result.append('FIV')
    for num in str_num:
        if num == 'SIX':
            result.append('SIX')
    for num in str_num:
        if num == 'SVN':
            result.append('SVN')
    for num in str_num:
        if num == 'EGT':
            result.append('EGT')
    for num in str_num:
        if num == 'NIN':
            result.append('NIN')

    answer = ' '.join(result)
    print("#{}\n{}".format(tc, answer))

# 1. if ONE이면 1로 ~ 계속 반복해서 글자를 숫자로
# 2. 글자와 숫자를 매핑
# str_to_number = {'ZRO': 0 ...}
# 3. Counting Sort
