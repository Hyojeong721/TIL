import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, h = input().split()
    h = '0x' + h
    h = bin(int(h, 16))[2:]
    if len(h) % 4:
        h = '0'+h
    print(f'#{tc} {h}')