import sys
sys.stdin = open('input.txt')

# 10 이 넘는 숫자를 위한 변환기
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T+1):
    N, number = input().split()
    # 최종 값 초기화
    result = ''
    # 뒤에서 부터 읽기
    for n in number[::-1]:
        # 알파벳은 숫자로 변환
        if n in converter:
            n = converter[n]
        # str타입으로 들어오는 숫자는 int로 변환
        n = int(n)
        # 16진수는 4자리 차지하니 4번 반복
        for _ in range(4):
            result = str(n % 2) + result
            n //= 2

    print("#{} {}".format(tc, result))