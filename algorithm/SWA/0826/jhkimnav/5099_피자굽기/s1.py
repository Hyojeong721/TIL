import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    answer = 0
    # N : 화덕의 크기, M : 피자 개수
    N, M = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    cIdx = 0
    oven = []

    # 화덕이 가득 찰 때까지 피자 넣기
    while cIdx < N:
        oven.append(cIdx)
        cIdx += 1

    # 화덕에 피자가 하나 남아있을 때 까지 반복
    while len(oven) != 1:
        check_idx = oven.pop(0)
        pizza[check_idx] = pizza[check_idx] // 2
        # 치즈가 아직 다 녹지 않았다면
        if pizza[check_idx]:
            oven.append(check_idx)
        else:
            # 화덕의 자리가 남아있고, 피자가 남았을 경우
            if len(oven) < N and cIdx < len(pizza):
                oven.append(cIdx)
                cIdx += 1

    print('#{} {}'.format(TC, oven[0]+1))