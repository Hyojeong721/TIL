import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()

    # A에 있는 B의 개수
    num = A.count(B)

    # (B의 길이 -1)
    # => B가 나오면 1번만 계산(A길이에서 B의 첫번째 글자를 뺀 나머지 글자수 * B가 나온 횟수 빼기)
    result = len(A) - (len(B)-1)*num

    print('#{} {}'.format(tc, result))
