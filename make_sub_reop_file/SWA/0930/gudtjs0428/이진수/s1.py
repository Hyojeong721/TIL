import sys
sys.stdin = open('input.txt')

def hex_to_bin(hexa):
    hexa_list = []
    for n in hexa:
        if n.isdigit():
            hexa_list.append(int(n))
        else:
            hexa_list.append(ord(n) - 55)
    bina = ''
    for i in range(len(hexa_list)-1, -1, -1):
        n = hexa_list[i]
        j = 0
        while j < 4:
            if n % 2:
                bina = '1' + bina
            else:
                bina = '0' + bina
            n //= 2
            j += 1
    return bina


T = int(input())
for test_case in range(1, T + 1):
    N, hexa = input().split()
    print('#{} {}'.format(test_case, hex_to_bin(hexa)))