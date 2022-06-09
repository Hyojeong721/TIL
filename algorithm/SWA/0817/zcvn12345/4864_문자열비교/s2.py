import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str2)
    M = len(str1)
    result = 0

    for i in range(N-M+1):
        if str1 == str2[i:i+M]:
            result += 1
            break

    print('#{} {}'.format(tc, result))