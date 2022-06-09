import sys
sys.stdin = open('input.txt')

def type_least(A, B):
    i = 0
    length_A = len(A)
    count = 0
    while i < len(A):
        if A[i:i + len(B)] == B:
            count += 1
            A = A[i + len(B):]
            i = 0
        else:
            i += 1
    return length_A - ((len(B) - 1) * count)

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    print('#{} {}'.format(tc, type_least(A, B)))