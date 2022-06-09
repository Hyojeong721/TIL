import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T + 1):
    origin = input()
    pipes = []
    pipe_number = 0
    # 쇠막대기가 레이저를 만난 횟수
    count_laser = 0

    i = 0
    while i < len(origin):
        # 열린 괄호를 만났을 때,

        if origin[i] == '(':

            if origin[i:i+2] == '()':
                if len(pipes) > 0:
                    count_laser += len(pipes)

                i += 2

            else:
                pipe_number += 1  # 쇠막대기 숫자 증가
                pipes.append(pipe_number)
                i += 1

        # 닫힌 괄호를 만났을 때, (쇠막대기의 끝)
        elif origin[i] == ')':
            # 가장 마지막 쇠막대기를 꺼낸다.
            pipes.pop()
            i += 1

    print('#{} {}'.format(tc, count_laser + pipe_number))