import sys
sys.stdin =open('input.txt')

T = int(input())

for tc in range(1, T+1):
# 문자열 길이 N인 str1 / M인 str2
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = 0

    for m in range(M-N):
        total=0
        for n in range(N):
            if str2[m+n] == str1[n]:
                total += 1
            if total == N:
                result = 1
    print('#{} {}'.format(tc, result))
