import sys
sys.stdin = open('input.txt')

def binary(a):
    if a in '0123456789':
        x = int(a)
    else:
        x = ord(a) - 55

    num = []
    for i in range(4):
        num.append(x % 2)
        x //= 2
    return list(reversed(num))

T = int(input())

for test_case in range(1, T+1):
    N, num_16 = input().split()

    num_2 = ''
    for number in num_16:
        tmp = binary(number)
        for i in range(4):
            num_2 += str(tmp[i])

    print('#{} {}'.format(test_case, num_2))