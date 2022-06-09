import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    for i in range(M-N+1):
        tmp = 0
        if str2[i] == str1[0]:
            for j in range(N):
                if str2[i+j] == str1[i]:
                    tmp += 1
        if tmp == N:
            break
    if tmp == N:
        print('#{} 1'.format(tc))

    else:
        print('#{} 0'.format(tc))