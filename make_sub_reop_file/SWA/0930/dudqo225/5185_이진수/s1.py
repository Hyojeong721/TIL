import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)

    # 2진수 값으로 저장
    bin_num = ''
    for number in hex_num:
        # 각 문자열을 10진수로 변환
        a = int(number, 16)
        # 10진수로 변환한 값을 2진수로 변환하고 자릿수를 4개로 맞춤
        bin_num += bin(a)[2:].zfill(4)

    # 결과 출력
    print('#{} {}'.format(tc, bin_num))
