import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()
    text = text.replace('()', 'B')
    cnt = 0
    total = 0
    for i in text:
        if i == '(':
            cnt += 1
            total += 1
        elif i == ')':
            cnt -= 1
        else:
            total = total + cnt

    print('#{} {}'.format(tc, total))