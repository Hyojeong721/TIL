import sys
sys.stdin = open('input.txt')

def change(n):
    n = n.strip('0.')
    return int(n) / 10 ** len(n)

def change_to_bin(n):
    result = ''
    while n > 0:
        result += str(n % 2)
        n //= 2
    return result[::-1]

T = int(input())
for tc in range(1, T+1):
    number = float(input())
    # number = change(number)
    cnt = 0
    while str(number)[len(str(number))-2:] != '.0':
        number *= 2
        cnt += 1
        if cnt >= 13:
            break
    # print(number, cnt)

    ans = str(change_to_bin(int(number)))
    if len(ans) != cnt:
        while len(ans) != cnt:
            ans = '0' + ans

    if len(ans) >= 13:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))




"""
1. 소수점 몇자리 째인지 먼저 기록
2. 소수점 없는 순수한 숫자를 뽑아내기
3. 그 숫자를 2진수로 변환
    625를 2진수로
"""