import sys

sys.stdin = open('input.txt')

# rstrip 이용해서 찾기
    # 마지막 자리 홀수 아니면 pass

# 축약하기기


ef convert(cipher):
    res = ''
    for x in cipher:
        num = int(x, 16)
        tmp = ''
        for i in range(3, -1, -1):
            if num & (1 << i):
                tmp += '1'
            else:
                tmp += '0'
        res += tmp

    return res


def brief(phrase, number):
    if number != 1:
        short = ''
        for idx, x in enumerate(phrase):
            if idx % number == 0:
                short += x
        return short
    else:
        return phrase


T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())  # N: 세로  M: 가로
    codes = [input().rstrip('0') for _ in range(N)]
    codes = [x for x in set(codes) if x != '']

    targets = []
    for code in codes:
        k = len(code) // 14
        for i in range(1, k+1):
            cut = code[len(code) - 14 * i:]
            targets.append(brief(convert(cut), k))
    print(targets)


    if tc == 10:
        break
