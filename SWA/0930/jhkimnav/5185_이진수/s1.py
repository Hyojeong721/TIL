import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, hex_str = input().split()
    bin_str = ''
    arr = []
    for c in hex_str:
        bin_str += format(int(c, 16), 'b').zfill(4)
    print('#{} {}'.format(tc, bin_str))