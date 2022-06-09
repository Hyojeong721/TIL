import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = 10
for tc in range(1, T + 1):
    i = int(input())
    kword = input()
    length = len(kw ord)
    text = input()
    cnt = 0
    for idx, value in enumerate(text):
        if value == kword[0]:
            if text[idx:idx + length] == kword:
                cnt += 1

    print('#{} {}'.format(i, cnt))
