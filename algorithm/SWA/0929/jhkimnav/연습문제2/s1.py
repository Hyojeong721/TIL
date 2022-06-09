import sys
sys.stdin = open('input.txt', 'r')

hex_str = input()
bin_str = ''

# 입력 : 16진수 형태의 문자열
# 1. 16진수 문자열 -> 10진수
# 2. format 함수로 2진수 변환
# 네 자리수로 고정시키기 위해 zfill() 사용

for c in hex_str:
    bin_str += format(int(c, 16), 'b').zfill(4)

N, reminder = divmod(len(bin_str), 7)
for i in range(N):
    print(int(bin_str[i*7:(i+1)*7], 2), end=', ')

if reminder > 0:
    print(int(bin_str[-reminder:], 2))

# print("2".zfill(4))
# 0002