import sys
sys.stdin = open('input.txt')

bits = input()
start = 0
ans = []

while start < len(bits):
    binary = bits[start:start+7]
    decimal = 0

    i = 1
    for bit in binary[::-1]:
        decimal += int(bit) * i
        i *= 2

    ans.append(str(decimal))
    start += 7

print(", ".join(ans))