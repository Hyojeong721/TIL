import sys
sys.stdin = open("input.txt", "r")

# 암호패턴
patterns = [
    '001101',  # 0
    '010011',  # 1
    '111011',  # 2
    '110001',  # 3
    '100011',  # 4
    '110111',  # 5
    '001011',  # 6
    '111101',  # 7
    '011001',  # 8
    '101111',  # 9
]

arr = input()
result = ''

for i in arr:
    num = int(i, 16)  # 16 -> 10
    for j in range(3, -1, -1):
        if num & (1 << j):
            result += '1'
        else:
            result += '0'

ans = []
i = 0
while i < len(result) - 5:
    check = result[i:i+6]
    if check in patterns:
        ans.append(str(patterns.index(check)))
        i += 6
    else:
        i += 1

print(', '.join(ans))













