import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    A, B = list(map(str, input().split()))

    text = A.replace(B, '*')

    print(f'#{test_case} {len(text)}')
