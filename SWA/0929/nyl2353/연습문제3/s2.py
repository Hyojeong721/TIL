import sys
sys.stdin = open('input.txt')

# 16진수 -> 2진수
num = list(input())
for i in range(len(num)):
    bi = format(int(num[i], 16), 'b')
    num[i] = '0' * (4 - len(bi)) + bi
num = ''.join(num)

pattern = ['001101', '010011', '111011', '110001',
           '100011', '110111', '001011', '111101',
           '011001', '101111']

# 암호 패턴 찾기
idx = 0
ans = ''
while idx < len(num):
    if num[idx:idx+6] in pattern:
        ans += str(pattern.index(num[idx:idx+6])) + ', '
        idx += 6
    else:
        idx += 1

# 출력 형태로 출력
ans = ans.rstrip(', ')
print(ans)