
import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(N):
    arr = input()
    arr = '9' + arr + '9'
    len_arr = len(arr)
    cnt, res = 0, 0

    for k in range(len_arr):
        if arr[k] == 'O':
            res += k-cnt
        else:
            cnt = k
    print(res)