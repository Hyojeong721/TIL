import sys
sys.stdin = open('input.txt')

# 상진스 코드 깔끔

def Forth(opers):
    nums = []
    for oper in opers:
        try:
            if int(oper):
                nums.append(int(oper))
        except:
            if oper == '+' or oper == '-' or oper == '/' or oper == '*':
                if len(nums) < 2:
                    return 'error'
                else:
                    if oper == '+':
                        nums.append(nums[-2] + nums[-1])
                        del nums[-3], nums[-2]
                    elif oper == '-':
                        nums.append(nums[-2] - nums[-1])
                        del nums[-3], nums[-2]
                    elif oper == '/':
                        nums.append(nums[-2] // nums[-1])
                        del nums[-3], nums[-2]
                    elif oper == '*':
                        nums.append(nums[-2] * nums[-1])
                        del nums[-3], nums[-2]
            elif oper == '.':
                if len(nums) != 1:
                    return 'error'
                else:
                    return nums[0]
            else:
                return 'error'


T = int(input())
for test_case in range(1, T + 1):
    opers = list(input().split())
    print('#{} {}'.format(test_case, Forth(opers)))