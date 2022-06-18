import sys
sys.stdin = open('input.txt')

num_16 = (' '.join(input())).split()

num_10 = []
tmp = 0

for i in range(len(num_16)):
    if num_16[i] in '012345679':
        tmp += int(num_16[i]) * (16 ** (6-(i%7)))
    else:
        tmp += (ord(num_16[i])-55) * (16 ** (6-(i%7)))

    if i % 7 == 6 or i == len(num_16) - 1:
        num_10.append(tmp)
        tmp = 0

print(num_10)