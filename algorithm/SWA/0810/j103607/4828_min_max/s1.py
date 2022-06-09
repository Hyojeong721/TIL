import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):

    case = int(input())
    case_numbers = list(map(int, input().split()))

    max = case_numbers[0]
    min = case_numbers[0]

    for num in case_numbers:
        if max <= num:
            max = num
        elif min > num:
            min = num

    result = max-min
    #print(f'#{tc} {result}')
    print('#{} {}'.format(tc, result))






