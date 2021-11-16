import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # N: 화덕의 크기 M: 피자 개수
    N, M = map(int, input().split())
    # 각 피자에 뿌려진 치즈 양
    cheese = list(map(int, input().split()))

    # (피자 번호, 치즈 양) 튜플로 cheese_idx에 저장
    cheese_idx = []   # 대기중인 피자
    for i, j in enumerate(cheese):
        cheese_idx.append((i, j))

    # 한번에 들어갈 수 있는 피자 수만큼 cheese_idx에서 뺴와서 pizza에 넣고 시작
    pizza = []
    for i in range(N):
        j = cheese_idx.pop(0)
        pizza.append(j)

    # pizza에 하나가 남을 때까지
    while len(pizza) > 1:
        a = pizza.pop(0)   # 첫번째 피자 (번호(idx), 치즈양(p))
        idx = a[0]
        p = a[1] // 2   # 치즈(p) // 2

        # 치즈가 0 이상이면 pizza에 다시 넣기
        if p > 0:
            pizza.append((idx, p))
        # 치즈가 0이 되면 다시 넣지 않고
        elif p == 0:
            # cheese_idx에 남은 피자가 없을 때까지 pop해서 pizza에 추가
            while cheese_idx:
                c = cheese_idx.pop(0)
                pizza.append(c)
                break

    # 피자 번호 = 인덱스 + 1
    print('#{} {}'.format(tc, pizza[0][0]+1))

