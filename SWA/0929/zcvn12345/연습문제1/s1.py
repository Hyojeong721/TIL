import sys
sys.stdin = open('input.txt')

binary = input()
temp = ''
for i in range(len(binary)):
    if i % 7 == 0 and i != 0:
        temp2 = 0
        for j in range(7):
            temp2 += (int(temp[j]) * (2**j))
        print(temp2)
        temp = ''
    temp += binary[i]