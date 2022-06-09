import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, hex  = input().split() # hex = 16진수
    N = int(N) # N = 자리수

    ans = ''
    for hex_single in hex:
        hex_single = '0x0' + hex_single
        # 1. 16진수를 10진수로 변환
        octal_number = int(hex_single, 16)
        # 2. 10진수를 2진수로 변환 
        binary_number = bin(octal_number)
        if len(binary_number) == 3:
            binary_number_no_b = '000' + binary_number.split('b')[1]
        elif len(binary_number) == 4:
            binary_number_no_b = '00' + binary_number.split('b')[1]
        elif len(binary_number) == 5:
            binary_number_no_b = '0' + binary_number.split('b')[1]
        else:
            binary_number_no_b = binary_number.split('b')[1]
        ans += binary_number_no_b
    print('#{} {}'.format(tc+1, ans))   
