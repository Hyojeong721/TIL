import sys
sys.stdin = open('input.txt')

T = int(input())
def num_2(num):
    output = ''
    for i in range(3,-1,-1):
        if num & (1<<i):
            output += '1'
        else:
            output += '0'
    return output

for tc in range(1,T+1):
    N, arr = input().split()

    print('#{}'.format(tc), end=' ')

    for n in range(int(N)):
        num_10 = int(arr[n],16)
        print(num_2(num_10), end='')
    print()
