import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    test_case, N = input().split()
    numbers = input().split()
    # print(test_case)
    # print(sorting(str_data))
    # 카운팅 정렬
    str_numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = [0] * 10
    for number in numbers:
        for i in range(10):
            if number == str_numbers[i]:
                result[i] += 1
    result_string = ''
    for i in range(10):
        result_string += (str_numbers[i] + ' ') * result[i]

    print('#{} {}'.format(tc, result_string))
###############################################
    # str_to_numbers = {
    #     'ZRO': 0,
    #     'ONE': 1,
    #     'TWO': 2,
    #     'THR': 3,
    #     'FOR': 4,
    #     'FIV': 5,
    #     'SIX': 6,
    #     'SVN': 7,
    #     'EGT': 8,
    #     'NIN': 9,
    # }
    #
    # int_to_numbers = {
    #     0: 'ZRO',
    #     1: 'ONE',
    #     2: 'TWO',
    #     3: 'THR',
    #     4: 'FOR',
    #     5: 'FIV',
    #     6: 'SIX',
    #     7: 'SVN',
    #     8: 'EGT',
    #     9: 'NIN',
    # }
    #
    # temp = []
    # for number in numbers:
    #     int_number = str_to_numbers[number]
    #     temp.append(int_number)
    # temp.sort()
    #
    # result = ''
    # for number in temp:
    #      result += int_to_numbers[number] + ' '
    # print('#{} {}'.format(tc, result))


# def sorting(data):
#     temp = data.replace('ZRO', '0')
#     temp = temp.replace('ONE', '1')
#     temp = temp.replace('TWO', '2')
#     temp = temp.replace('THR', '3')
#     temp = temp.replace('FOR', '4')
#     temp = temp.replace('FIV', '5')
#     temp = temp.replace('SIX', '6')
#     temp = temp.replace('SVN', '7')
#     temp = temp.replace('EGT', '8')
#     temp = temp.replace('NIN', '9')
#
#     int_list = temp.split(' ')
#     int_list.remove('')
#     result = list(map(int, int_list))
#     result.sort()
#     result = list(map(str, result))
#     result = ' '.join(result)
#
#     temp = result.replace('0', 'ZRO')
#     temp = temp.replace('1', 'ONE')
#     temp = temp.replace('2', 'TWO')
#     temp = temp.replace('3', 'THR')
#     temp = temp.replace('4', 'FOR')
#     temp = temp.replace('5', 'FIV')
#     temp = temp.replace('6', 'SIX')
#     temp = temp.replace('7', 'SVN')
#     temp = temp.replace('8', 'EGT')
#     temp = temp.replace('9', 'NIN')
#
#     return temp
###########################################

# T = int(input())
#
# # 정렬용 알파벳
# number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for tc in range(1, 1 + T):
#
#     n = list(map(str, input().split()))
#
#     # 무작위 숫자 리스트
#     number_list = list(map(str, input().split()))
#
#     # 개수 체크용
#     res = [0] * 10
#
#     for q in number_list:
#         res[number_alpha.index(q)] += 1
#
#     print(n[0])
#     for w in range(10):
#         print('{} '.format(number_alpha[w]) * res[w])

#######################################################