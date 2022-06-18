import sys
sys.stdin = open('input.txt')


# 연습문제 2의 함수 재활용
def hex_to_bin(hex_num):
    """
    1자리 16진수 수('0' ~ '9' / 'A' ~ 'F')를 2진수 수로 바꾼다.
    Returns:
        bin_num: 2진수 수
        (단, 앞의 0b는 없애고, 반드시 4자리로 반환한다. ex. 0b10 => 0010)
    """
    # 1. 16진수 => 10진수
    dec = int(hex_num, 16)
    # 2. 10진수 => 2진수 (앞의 '0b'를 없애고, 4자리로 만들어준다.)
    bin_num = bin(dec)[2:].zfill(4)
    return bin_num


# 암호 비트 패턴 (codes[i]는 i의 패턴)
codes = [
    '001101', '010011', '111011', '110001', '100011',
    '110111', '001011', '111101', '011001', '101111',
]

hex_code = input()
bin_code = ""

for num in hex_code:
    bin_code += hex_to_bin(num)

# 암호의 시작 인덱스를 찾는다.
start = 0

while start < len(bin_code):
    if bin_code[start:start + 6] in codes:
        break
    start += 1

for i in range(start, len(bin_code), 6):
    current = bin_code[i:i + 6]
    for j in range(10):
        # 암호문을 찾은 경우 => 해당 암호의 숫자를 출력하고, for문을 빠져나온다.
        if current == codes[j]:
            print(j, end=" ")
            break
    # 암호문을 찾지 못한 경우 => 탐색을 종료한다.
    else:
        break
