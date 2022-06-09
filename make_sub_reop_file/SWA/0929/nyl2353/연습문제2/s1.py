import sys
sys.stdin = open('input.txt')

def hex2bi(char):
    """
    16진수 문자 1개를 입력으로 받아, 2진수 문자열로 반환

    """
    diff = ord('A') - ord('0')
    ans = ''

    if ord('0') <= ord(char) <= ord('9'):
        deci = int(char)
    else:
        deci = int(chr(ord(char) - diff)) + 10
    for i in range(3, -1, -1):
        ans += "1" if deci & (1 << i) else "0"

    return ans

# 16진수 문자열 -> 2진수 문자열
hexa = input()
bi = ''
for i in hexa:
    bi += hex2bi(i)

# 2진수 문자열 7bits 씩 10진수로 변환 후 출력
start = 0
ans = []
while start < len(bi):
    binary = bi[start:start+7]
    decimal = 0

    i = 1
    for bit in binary[::-1]:
        decimal += int(bit) * i
        i *= 2

    ans.append(str(decimal))
    start += 7

print(", ".join(ans))