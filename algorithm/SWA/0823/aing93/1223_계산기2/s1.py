for tc in range(10):
    n = int(input())
    board = list(map(str, input()))
    # 연산자 + * 저장
    cal = []
    # 숫자 저장
    num = []

    for q in board:
        if q == '+' or q == '*':
            cal.append(q)

        else:
            num.append(int(q))