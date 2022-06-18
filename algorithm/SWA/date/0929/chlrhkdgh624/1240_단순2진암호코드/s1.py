import sys
sys.stdin = open("input.txt", "r")

patterns = [
    '3211',  # 0
    '2221',  # 1
    '2122',  # 2
    '1411',  # 3
    '1132',  # 4
    '1231',  # 5
    '1114',  # 6
    '1312',  # 7
    '1213',  # 8
    '3112',  # 9
]


# 56개씩 자르는 함수
def cutting(full_code, total):
    res = []
    for i in range(total-56):
        res.append(full_code[i:i+56])
    return res


# 치환하는 함수
def change(digit7):
    i = 1
    start = digit7[0]
    length = 1
    res = ''
    while i < 7:
        if digit7[i] == start:
            i += 1
            length += 1
        else:
            res += str(length)
            start = digit7[i]
            length = 1
            i += 1
        if i == 7:
            res += str(length)
            break
    return  res


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 세로, M: 가로
    arr = [input() for _ in range(N)]

    cipher = ''  # 암호문
    for code in arr:
        if '1' in code:
            cipher = code
            break

    targets = cutting(cipher, M)

    result = []
    for target in targets:
        before = []
        for j in range(8):
            check = change(target[7*j:7*j+7])
            if check in patterns:
                before.append(check)
            else:
                break
        if len(before) == 8:
            result.extend(before)

    result = [patterns.index(x) for x in result]

    odd = 0
    even = 0
    for i in range(8):
        if i & 1 == 0:
            odd += 3*result[i]
        else:
            even += result[i]

    ans = 0
    if (odd + even) % 10 == 0:
        ans += sum(result)

    print('#{} {}'.format(tc, ans))


