import sys
sys.stdin = open('input.txt')

def get_sum_codes(N, M, matrix):
    sum_codes = 0
    codes = []
    # 암호는 세로길이가 최소5라 했으니 밑에서 5번째 줄까지만 확인하면 됨
    for i in range(N-1-4):
        j = 1
        # 모두 16진수여도 56을 채우려면 14개는 필요하기때문에 뒤에서 14번째까지만 0인지 아닌지 확인하면 됨
        while j < M - 1-14:
            code = ''
            h = matrix[i][j]
            # 0이 아닐시
            if h != '0':
                # (각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.)
                while j < M - 1 - 1:
                    code += h
                    j += 1
                    h = matrix[i][j]
                    if h == '0' and matrix[i][j+1] == '0':
                        break
            if code and code not in codes:
                codes.append(code)
            else:
                j += 1

    for code in codes:
        bina = ''
        for n in code:
            tmp = ''
            if n.isdigit():
                n = int(n)
            else:
                n = ord(n) - 55
            for _ in range(4):
                if n % 2:
                    tmp = '1' + tmp
                else:
                    tmp = '0' + tmp
                # tmp = str(n % 2) + tmp
                n //= 2
            bina += tmp

        # strip
        while bina[-1] == '0':
            bina = bina[:-1]
        length = len(bina)
        len_divider = length // 56
        sum_lasts = sum(map(int, bina[:-4 * len_divider + 1:-1]))
        while sum_lasts > len_divider * 4:
            bina = bina[:-1]
        if length > 56 * len_divider:
            bina = bina[-56 * len_divider:]
        if bina and bina not in codes:
            code = []
            for k in range(8):
                tmp = bina[k * 7 * len_divider :k * 7 * len_divider + 7 * len_divider ]
                if tmp == '000' * len_divider + '11' * len_divider + '0' * len_divider + '1' * len_divider:
                    code.append(0)
                    continue
                if tmp == '00' * len_divider + '11' * len_divider + '00' * len_divider + '1' * len_divider:
                    code.append(1)
                    continue
                if tmp == '00' * len_divider + '1' * len_divider + '00' * len_divider + '11' * len_divider:
                    code.append(2)
                    continue
                if tmp == '0' * len_divider + '1111' * len_divider + '0' * len_divider + '1' * len_divider:
                    code.append(3)
                    continue
                if tmp == '0' * len_divider + '1' * len_divider + '000' * len_divider + '11' * len_divider:
                    code.append(4)
                    continue
                if tmp == '0' * len_divider + '11' * len_divider + '000' * len_divider + '1' * len_divider:
                    code.append(5)
                    continue
                if tmp == '0' * len_divider + '1' * len_divider + '0' * len_divider + '1111' * len_divider:
                    code.append(6)
                    continue
                if tmp == '0' * len_divider + '111' * len_divider + '0' * len_divider + '11' * len_divider:
                    code.append(7)
                    continue
                if tmp == '0' * len_divider + '11' * len_divider + '0' * len_divider + '111' * len_divider:
                    code.append(8)
                    continue
                if tmp == '000' * len_divider + '1' * len_divider + '0' * len_divider + '11' * len_divider:
                    code.append(9)
                    continue
            if ((code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]) % 10 == 0:
                sum_codes += sum(code)
    else:
        j += 1
    return sum_codes


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [ list(input()) for _ in range(N)]
    print('#{} {}'.format(test_case, get_sum_codes(N, M, matrix)))