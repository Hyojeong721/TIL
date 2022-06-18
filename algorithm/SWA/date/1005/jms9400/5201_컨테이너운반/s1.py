import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N 컨테이너수  M 트럭 수
    wi = sorted(list(map(int, input().split())), reverse=True)  # 화물 무게
    ti = sorted(list(map(int, input().split())), reverse=True)  # 트럭 적재용량
    answer = 0
    a = ti.pop(0)

    while True:
        if wi:
            b = wi.pop(0)
        else:
            break

        if a >= b:
            answer += b
            if ti:
                a = ti.pop(0)
            else:
                break

    print('#{} {}'.format(tc, answer))

