import sys
sys.stdin = open('input.txt')


'''
잘못 푼거
'''

T = int(input())
for test_case in range(1, T+1):

    N, M = list(map(int, (input().split())))
    # N = case[0] # 총 숫자 개수
    # M = case[1] # 그 중에서 연속되는 숫자 개수

    case_numbers = list(map(int, input().split()))

    max = sum(case_numbers[0:M])
    min = sum(case_numbers[0:M])

    for i in range(N-M+1): # i = 0~7 / 0~

        total = 0
        for n in case_numbers[i+1:i+M+1]:
            total += n
            if max < total:
                max = total
            elif min > total:
                min = total

        result = max - min
    print(result)
    #print(f'#{test_case} {result}')
