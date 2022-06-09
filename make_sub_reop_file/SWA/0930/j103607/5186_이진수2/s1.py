import sys
sys.stdin = open('input.txt')



TC = int(input())
for tc in range(1, TC+1):
    N = float(input())

    count = 0   # 소수점 아래 자리수
    result = ''   # 소수점 아래 숫자

    a = 1
    while N:
        if N < 2**-a:
            result += '0'
        else:
            N -= 2**-a
            result += '1'
        count += 1

        if count > 12:
            result = 'overflow'
            break
        else:
            a += 1

    print('#{} {}'.format(tc, result))


