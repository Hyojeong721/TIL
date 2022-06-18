import sys
sys.stdin = open("input.txt")


T = 10

for _ in range(T):
    tc = int(input())
    queue = [int(x) for x in input().split()]

    i = 0

    while True:
        # cnt: 큐의 마지막에 넣을 수
        #      = 큐의 맨 앞에서 뺀 수에 현재 사이클의 숫자(1 ~ 5)를 뺀 수
        cnt = queue.pop(0) - (i + 1)

        # 큐의 마지막에 넣을 수(cnt)가 0 이하면, 큐에 0을 넣고 반복을 종료한다.
        if cnt <= 0:
            queue.append(0)
            break
        # cnt가 0보다 크다면, 큐에 해당 숫자를 넣고 탐색을 계속 진행한다.
        queue.append(cnt)
        # i는 반복문을 돌며 0 ~ 4를 반복한다.
        # 이는 큐에서 뺀 수에서 감소시켜야 할 수보다 1 작으므로,
        # 실제로는 큐에서 뺀 수에서 (i + 1)를 뺀다.
        i = (i + 1) % 5

    # 큐에 있는 수들을 문자로 바꾼 뒤, 공백문자로 구분하여 출력한다.
    print("#{} {}".format(tc, " ".join(map(str, queue))))
