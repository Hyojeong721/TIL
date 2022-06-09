import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    case = list(map(str, input().split()))

    number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nums = list(map(str, input().split()))
    for i in range(len(nums)):
        for j in range(len(number)):
            if nums[i] == number[j]:
                cnt[j] += 1

    num_list = []
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            num_list.append(number[i])
            num_list.append(' ')

    answer = ''.join(num_list)

    print(f'{case[0]}')
    print(answer)











