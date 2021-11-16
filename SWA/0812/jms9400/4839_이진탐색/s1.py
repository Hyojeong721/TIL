import sys
sys.stdin = open('input.txt')

T = int(input())

# 이진탐색 함수
def find_page(N, P):
    l = 1
    r = N
    result = 0
    while l <= r:
        c = int((l+r)/2)
        # result값을 각각의 if 내에 넣을 필요없이 처음에 한번만 주면 됨
        result += 1
        if P == c:
            return result
        elif P < c:
            r = c
        else:
            l = c

for tc in range(1, T + 1):
    N, A, B = list(map(int, input().split()))

    # 찾은 횟수가 적은 사람의 이름 출력
    if find_page(N, A) < find_page(N, B):
        print('#{} A'.format(tc))
    elif find_page(N, A) == find_page(N, B):
        print('#{} 0'.format(tc))
    else:
        print('#{} B'.format(tc))
