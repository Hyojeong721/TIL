import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = list(input().split())
    a = len(A)
    b = len(B)
    enter = 0
    k = 0
    i = 0

    # 문자를 비교하는 시작점이 문자길이보다 작은경우 반복!
    while i + k < a:
        # B의 문자길이만큼 A의 문자열을 잘라서 비교
        if A[i + k: i + k + b] == B:
            enter += 1
            k += b - 1  # 같을 경우 다음 비교하는 자리로 점프
            i += 1
        else:
            enter += 1
            i += 1

    print('#{} {}'.format(tc, enter))