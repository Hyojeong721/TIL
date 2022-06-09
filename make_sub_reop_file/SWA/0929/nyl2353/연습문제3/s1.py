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

pattern = ['001101', '010011', '111011', '110001',
           '100011', '110111', '001011', '111101',
           '011001', '101111']

# 암호 패턴 찾아 출력 형태로 출력
start = 0
ans = []
while start < len(bi):
    temp = bi[start:start+6]

    is_pattern = False
    for i, p in enumerate(pattern):
        if temp == p:
            ans.append(str(i))
            is_pattern = True
            break
    if is_pattern:
        start += 6
    else:
        start += 1

print(", ".join(ans))
