import sys
sys.stdin = open('input.txt')

numbers = input()

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

num = ''
for i in numbers:
    if i.isdigit():
        n = str(bin(int(i)))[2:]

        if len(n) != 4:
            temp = n
            while len(temp) != 4:
                temp = '0' + temp
            n = temp
        num += n
    else:
        n = str(bin(dic[i]))[2:]
        # if len(n) != 4:
        #     while len(n) != 4:
        #         n[::-1] += '0'
        num += n
for i in range(0, len(num), 7):
    if i+7 < len(num):
        print(int(num[i:i+7], 2), end=' ')
    else:
        print(int(num[i:], 2), end=' ')




"""

0000 1111 1001 0111 1010 0011

"""

