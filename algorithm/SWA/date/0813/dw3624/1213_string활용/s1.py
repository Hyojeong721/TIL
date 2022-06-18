import sys
sys.stdin = open('input.txt', encoding = 'utf-8')

# T = 10
# for t in range(T):
#     t = int(input())
#     char = input()
#     text = input()
#     result = text.count(char)
#
#     print('#{} {}'.format(t, result))


T = 10
for t in range(T):
    t = int(input())
    char = input()
    text = input()
    n, idx = len(char), len(char)
    cnt = 0

    while idx <= len(text):
        if text[idx - n:idx] == char:
            cnt += 1
        idx += 1

    print('#{} {}'.format(t, cnt))
