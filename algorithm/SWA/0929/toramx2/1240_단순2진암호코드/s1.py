import sys
sys.stdin = open('input.txt')

PATTERN= {
    '0': '0001101',
    '1': '0011001',
    '2': '0010011',
    '3': '0111101',
    '4': '0100011',
    '5': '0110001',
    '6': '0101111',
    '7': '0111011',
    '8': '0110111',
    '9': '0001011',
}

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    code = ''
    for _ in range(N):
        code += input()


    answer = ''
    i = 0
    while i + 7 < len(code):
        for j in range(len(PATTERN)):
            if code[i:i + 7] == PATTERN[str(j)]:
                answer += str(j)
                i += 6
                break
        i += 1




    pw = answer[0:8]
    cert_odd = 0
    cert_even = 0
    for i in range(0, len(pw), 2):
        cert_odd += int(pw[i])
    for i in range(1, len(pw), 2):
        cert_even += int(pw[i])

    cert = cert_odd * 3 + cert_even

    if cert % 10 == 0:
        result = cert_odd + cert_even
    else:
        result = 0

    print('#{} {}'.format(test_case, result))