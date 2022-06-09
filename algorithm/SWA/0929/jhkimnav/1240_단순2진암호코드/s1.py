import sys
sys.stdin = open('input.txt', 'r')

def decode(code):
    dict = {
        '0001101': 0, '0011001': 1,
        '0010011': 2, '0111101': 3,
        '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9,
    }


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] * M
    for i in range(N):
        if
            arr[i] = input().rstrip('0')[-56:-1]
            print(arr[i])


