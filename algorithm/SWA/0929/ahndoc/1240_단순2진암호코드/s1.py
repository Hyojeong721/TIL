import sys
sys.stdin = open('input.txt')

def check(data):
    patterns = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(10):
        if data == patterns[i]:
            return i
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    for data in arr:
        if '1' in data:
            end_idx = data.rfind('1')
            start_idx = end_idx - 55
            data = data[start_idx:end_idx+1]
            break

    my_patterns = []
    for i in range(0, len(data), 7):
        my_patterns.append(check(data[i:i+7]))

    ans = 0
    odd_total = 0
    even_total = 0
    for i in range(4):
        odd_total += my_patterns[i*2]
        even_total += my_patterns[i*2+1]

    if (odd_total * 3 + even_total) % 10 == 0:
        ans = sum(my_patterns)
        print('#{} {}'.format(tc, ans))
    else:
        print('#{} {}'.format(tc, ans))





