import sys
sys.stdin = open('input.txt')

def change(n):
    result = ''
    while n > 0:
        result += str(n % 2)
        n //= 2

    if len(result) != 4:
        while len(result) != 4:
            result += '0'

    return result[::-1]

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()
    ans = ''
    for i in range(int(N)):
        if N16[i].isdigit():
            n = int(N16[i])
            ans += change(n)
        else:
            n = dic[N16[i]]
            ans += change(n)
    print('#{} {}'.format(tc, ans))