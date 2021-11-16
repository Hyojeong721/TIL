import sys
sys.stdin = open('input.txt', 'r')

bin_str = input()
N = len(bin_str)
for i in range(N // 7):

    # 2진수 형태의 문자열 -> 10진수
    print(int(bin_str[i*7:(i+1)*7], 2), end=', ')
