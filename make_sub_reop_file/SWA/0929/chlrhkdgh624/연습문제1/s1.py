import sys
from math import ceil
sys.stdin = open('input.txt', 'r')

binary = list(input())
k = ceil(len(binary)/7)  # ceil = 올림
result = []
for i in range(k):
    output = '0b'  # '0b'
    for j in range(7*i, 7*(i+1)):
        output += binary[j]
    result.append(str(int(output, 2)))
    # int(value, num): num 진법인 수 value를 10진수로
print(",".join(result))


