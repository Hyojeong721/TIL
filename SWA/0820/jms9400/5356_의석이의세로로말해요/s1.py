import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    word_list = [list(input()) for _ in range(5)]
    word_len = []

    result = ''

    for i in range(5):
        word_len.append(len(word_list[i]))
    max_len = max(word_len)

    for i in range(max_len):
        for j in range(5):
            if word_len[j] > i:
                result += word_list[j][i]

            # try:
            #     print(word[j][i], end="")
            # except:
            #     pass
    print('#{} {}'.format(tc, result))