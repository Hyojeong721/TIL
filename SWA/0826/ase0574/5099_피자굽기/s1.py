import sys
sys.stdin = open('input.txt')
# 주어진 조건에 따라 피자를 구울 때,
# 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램
T = int(input())

for tc in range(1, T + 1):
    # 화덕의 크기 N과 피자 개수 M
    N, M = list(map(int, input().split()))
    pizza = list(map(int, input().split()))

    queue = []
    # 화덕에 피자 채우기
    for i in range(N):
        queue.append((i,pizza[i]))

    # 다음 넣을 피자의 인덱스
    index = N

    # 화덕에 피자가 한개만 남아있을 때까지 반복
    while len(queue) >= 2:
            # 화덕 한바퀴
        for j in range(len(queue)):
            # 화덕에 피자 갯수 확인
            if len(queue) >= 2:
                front = queue.pop(0)
            else:
                break

            # 치즈양 0 이면 뺀상태로
            if front[1] <= 0:
                if index < M:
                    queue.append((index, pizza[index]))
                    index += 1
            # 치즈양이 0이 아니면 맨뒤로
            else:
                queue.append(front)

        # 치즈 양 반으로 줄이기
        for k in range(len(queue)):
            front_pizza = queue.pop(0)
            pizza_index = front_pizza[0]
            half_pizza = front_pizza[1]//2
            queue.append((pizza_index, half_pizza))

    last_pizza = queue[0][0] + 1
    print("#{} {}".format(tc, last_pizza))