import sys
sys.stdin = open("input.txt")


def get_last_pizza(cheeses, N, M):
    """
    각 피자의 치즈 양이 주어질 때, 화덕에 마지막까지 남아있는 피자 번호를 구한다.
    (피자가 M개일 때, 피자 번호는 1번 ~ M번이다.)
    Args:
        cheeses: 1번 ~ M번 피자의 치즈의 양 (정수 배열)
        N: 화덕의 크기
        M: 피자의 개수
    Returns:
        last_pizza: 화덕에 마지막까지 남아있는 피자의 번호
    """
    # 원형 큐를 통해 화덕을 구현
    # 큐에는 [피자 번호, 치즈의 양] 형태로 값이 들어감.
    oven = [[0, 0] for _ in range(N)]
    """
    front: 원형 큐의 탐색 위치
    idx: 다음 화덕에 자리가 날 때 넣을 피자의 인덱스
    count: 화덕에 넣었다가 꺼낸 피자의 개수
    """
    front = 0
    idx, count = 0, 0

    # 전체 피자를 화덕에 넣었다가 꺼낼때까지 반복한다.
    while count < M:
        front = (front + 1) % N
        # 현재 탐색중인 화덕 위치가 비어있고
        if not oven[front][0]:
            # 넣을 피자가 남아있다면
            if idx < M:
                # (피자 번호, 치즈의 양)을 삽입한다.
                oven[front] = [idx + 1, cheeses[idx]]
                idx += 1
        # 현재 탐색중인 화덕 위치가 비어있지 않다면
        else:
            # 치즈의 양을 절반(x // 2)으로 만든다.
            oven[front][1] //= 2
            # 만약 치즈의 양이 0이라면
            if not oven[front][1]:
                # 현재 피자를 꺼낸다.
                last_pizza = oven[front][0]
                oven[front] = [0, 0]
                count += 1

                # 넣을 피자가 남아있다면 새로운 피자를 넣는다.
                if idx < M:
                    oven[front] = [idx + 1, cheeses[idx]]
                    idx += 1

    return last_pizza


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = [int(x) for x in input().split()]

    last_pizza = get_last_pizza(cheeses, N, M)

    print("#{} {}".format(tc, last_pizza))
