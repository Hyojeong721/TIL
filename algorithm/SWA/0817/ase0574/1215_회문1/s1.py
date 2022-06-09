import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    print(arr)
    for row in arr:
        for i in range(9-N):
            if row[i:i+N] == row[i:i+N][::-1]:
                cnt += 1

    for col in range(8):
        temp = ''
        for i in arr:
            temp += i[col]
        for j in range(9-N):
            if temp[j:j+N] == temp[j:j+N][::-1]:
                cnt += 1

    print('#{0} {1}'.format(tc, cnt))