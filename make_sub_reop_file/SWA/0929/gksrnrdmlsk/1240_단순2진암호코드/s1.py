import sys
sys.stdin = open('input.txt')

T = int(input())
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    cnt = 0
    word = ''
    for _ in range(N):
        temp = input()
        if cnt == 60:
            continue

        else:
            if word:
                if 60 - cnt == M:
                    word += temp[:60 - cnt]
                    cnt = 60
                else:
                    word += temp
                    cnt += M

            else:
                for i in range(M):
                    if temp[i] == '0':
                        pass
                    else:
                        word += temp[i - 3:]
                        if len(word) < 60:
                            cnt = len(word)
                            break
                        else:
                            word = word[:60]
                            cnt = 60
    while word[7] != '0' or code.get(word[0:7], -1) == -1:
        word = word[1:]
        continue

    word = word[:56]
    result = 0
    for i in range(8):
        value = code[word[7 * i: 7 * (i + 1)]]

        if i % 2 == 0:
            answer += value
            result += 3 * value
        else:
            answer += value
            result += value


    if result % 10:
        print('#{} {}'.format(tc, 0))

    else:
        print('#{} {}'.format(tc, answer))
