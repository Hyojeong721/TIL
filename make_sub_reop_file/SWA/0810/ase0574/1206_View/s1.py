import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = list(map(int,input().split()))
    bh = list(map(int,input().split()))
    result = 0

    for i in range(2, len(bh)-2):
        if bh[i-2] > bh[i-1]:
            left = bh[i-2]
        elif bh[i-2] <= bh[i-1]:
            left = bh[i-1]

        if bh[i+2] > bh[i+1]:
            right = bh[i+2]
        elif bh[i+2] <= bh[i+1]:
            right = bh[i+1]

        left_result = bh[i] - left
        right_result = bh[i] - right

        if left_result >= right_result:
            temp = right_result
        else:
            temp = left_result

        if temp > 0:
            result += temp


    print('#{} {}'.format(tc, result))
