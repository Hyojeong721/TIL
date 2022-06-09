import sys
sys.stdin = open('input.txt')


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    power = 'OFF'
    """
    M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있다.
    <=> M을 2 ** N으로 나눈 나머지가 2 ** N - 1이다.
    (뒤에서 N + 1번째 비트부터는 모두 2 ** N의 배수)
    ( 2^0 + 2^1 + ... + 2^n = 2^(n+1) )
    """
    if M % (2 ** N) == 2 ** N - 1:
        power = 'ON'

    print("#{} {}".format(tc, power))
