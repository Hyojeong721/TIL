import sys
sys.stdin = open('input.txt')

def binary(N, digit, ans):
    if N == 0:
        return ans
    if digit == 13:
        return 'overflow'
    if N >= (2 ** digit):
        ans += '1'
        N -= (2 ** digit)
        digit -= 1
        return binary(N, digit, ans)
    else:
        ans += '0'
        digit -= 1
        return binary(N, digit, ans)


T = int(input())
for tc in range(T):
    N = float(input())
    ans = '0.'
    print(binary(N, -1, ans))