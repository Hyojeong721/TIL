import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    tmp = 0
    cnt = 0
    for s1 in str1:
        tmp = 0
        for s2 in str2:
            if s1 == s2:
                tmp += 1
        if cnt < tmp:
            cnt = tmp

    print('#{} {}'.format(t, cnt))