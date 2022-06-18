import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    # 문자열 A안에 B를 띄어쓰기로 바꿔서 길이를 출력
    A = A.replace(B, ' ')
    print('#{0} {1}'.format(tc, len(A)))