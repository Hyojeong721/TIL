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

num_16 = (' '.join(input())).split()

code = ''
for number in num_16:
    tmp = binary(number)
    for i in range(4):
        code += str(tmp[i])


pattern = {
    '0': '001101',
    '1': '010011',
    '2': '111011',
    '3': '110001',
    '4': '100011',
    '5': '110111',
    '6': '001011',
    '7': '111101',
    '8': '011001',
    '9': '101111',
}

# print(pattern['7'])''
# print(code[0:20])

answer = ''
i = 0
while i+6 < len(code):
    for j in range(len(pattern)):
        if code[i:i+6] == pattern[str(j)]:
            answer += str(j)
            i += 5
            break
    i += 1

print(answer)