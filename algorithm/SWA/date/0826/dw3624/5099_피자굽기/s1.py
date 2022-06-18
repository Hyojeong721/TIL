import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # pizza 딕셔너리 생성
    ## {피자번호 : [치즈량, 화덕 내 이동횟수], ...}
    pizza = {}
    for i in range(1, M+1):
        pizza[i] = [cheese[i-1], 0]
    print(pizza)

    # 피자 번호 생성 후 N 만큼 pop, que 생성
    que = []
    pizza_no = list(range(1, M+1))
    for n in range(N):
        que.append(pizza_no.pop(0))


    # que 내부에 요소가 1개 남을 때까지 반복
    while len(que) > 1:
        v = que.pop(0)    # que에서 피자 번호 pop
        pizza[v][1] += 1  # 해당 번호 피자의 이동횟수 1 증가

        if pizza[v][1] == 3:    # 이동횟수가 3이 된 경우
            pizza[v][1] = 0     # 이동횟수 reset
            pizza[v][0] //= 2   # 치즈량 반으로

        if pizza[v][0] <= 0:    # 치즈량이 0 이하가 됐을 때
            if pizza_no:        # 피자번호 리스트에 값이 있는 경우
                que.append(pizza_no.pop(0))     # 피자번호 pop, que에 추가
            continue    # v를 append 하지않고 다음으로

        que.append(v)

    print('#{} {}'.format(tc, *que))