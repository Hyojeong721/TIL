import sys
sys.stdin = open('input.txt')

h = input()
h = '0x' + h
h = int(h, 16)
h = bin(h)[2:]


def trans(binary):
    temp = ''
    for i in range(len(binary)):
        if i % 7 == 0 and i != 0:
            temp2 = 0
            for j in range(7):
                temp2 += (int(temp[j]) * (2 ** j))
            print(temp2)
            temp = ''
        temp += binary[i]

trans(h)


