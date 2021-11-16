import sys
sys.stdin = open('input.txt')


T = int(input())

for TC in range(1, T+1):
    answer = 0
    # A : 타이핑할 문자열
    # B : 검색할 문자열
    A, B = input().split()
    cnt = A.count(B)

    #
    answer = len(A) - ((len(B) - 1) * cnt)

    print('#{} {}'.format(TC, answer))