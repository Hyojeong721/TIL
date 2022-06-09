import sys
sys.stdin = open('input.txt')

num_2 = (' '.join(input())).split()

num_10 = []
tmp = 0

for i in range(len(num_2)):
    tmp += int(num_2[i]) * (2 ** (6-(i%7)))
    if i % 7 == 6 or i == len(num_2) - 1:
        num_10.append(tmp)
        tmp = 0

print(num_10)

