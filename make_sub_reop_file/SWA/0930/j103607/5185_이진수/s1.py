import sys
sys.stdin = open('input.txt')


# T = int(input())
# for tc in range(1, T+1):

    # nums = input()
    # result = '0' + bin(int(nums[2:], 16))[2:]
    # print('#{} {}'.format(tc, result))



Patterns = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9, 'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}


TC = int(input())
for tc in range(1, TC+1):
    N, nums = map(str, input().split())

    result = ''
    for i in nums:

        # 이렇게 하니까 런타임에러 뜸
        # if i in '123456789':
        #     num = int(i)
        # else:
        #     num = Patterns[i]

        num = Patterns[i]

        temp = ''
        for j in range(4):
            q = num // 2
            r = num % 2
            temp = str(r) + temp
            num = q
        result += temp


    print('#{} {}'.format(tc, result))

