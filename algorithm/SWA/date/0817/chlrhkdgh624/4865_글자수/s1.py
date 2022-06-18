import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = set(input())
    str2 = input()
    result = 0

    for letter in str1:
        cnt = 0
        for x in str2:
            if letter == x:
                cnt += 1
        if cnt > result:
            result = cnt

    print(f'#{tc} {result}')
