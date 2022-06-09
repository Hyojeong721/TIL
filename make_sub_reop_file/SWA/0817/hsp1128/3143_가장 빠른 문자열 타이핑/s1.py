import sys
sys.stdin = open('input.txt')
T = int(input())

def min_num(A, B):
    result = 0
    tmp_cnt = 0
    tmp = 0
    for i in range(len(A)-len(B)+1):
        if A[i] == B[0]:
            for k in range(len(B)):
                if A[i+k] == B[k]:
                    tmp += 1
            if tmp == len(B):
                tmp_cnt += 1

    result = len(A) - tmp + tmp_cnt
    return result




for tc in range(1, T+1):
    A, B = input().split()
    print('#{} {}'.format(tc, min_num(A, B)))

