import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    code_pattern = [
        '0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011',
    ]

    # 암호코드 찾기
    code = ''
    for i in range(N):
        if '1' in arr[i]:
            for j in range(M):
                code += arr[i][j]
            break

    # 56자리 코드로 자르기
    rev_code = code[::-1]
    for i in range(len(rev_code)):
        if rev_code[i] == '1':
            rev_code = rev_code[i:i+56]
        break
    code = rev_code[::-1]

    print(code)
    code_num = [
        code[0:7],
        code[7:14],
        code[14:21],
        code[21:28],
        code[28:35],
        code[35:42],
        code[42:49],
        code[49:56],
    ]

    for i in range(8):
        code_num[i] = code_pattern.index(code_num[i])

    sum_odd = code_num[0] + code_num[2] + code_num[4] + code_num[6]
    sum_even = code_num[1] + code_num[3] + code_num[5]
    res = (sum_odd * 3) + sum_even + code_num[7]

    if res % 10 == 0:
        print('#{} {}'.format(tc, sum(code_num)))
    else:
        print('#{} {}'.format(tc, 0))