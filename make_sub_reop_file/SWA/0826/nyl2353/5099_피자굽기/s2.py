'''

Fail (8개만 통과)

순서대로 하나씩 검사하는 조건을 놓쳐서 한 번에 모두 검사하는 방식으로 구현했다.
그래서 test case에서 걸린 것 같다.

s1에서 queue를 이용해 하나씩 검사하도록 구현한 게 훨씬 간단하다.

'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N: 화덕크기, M: 피자개수, C: 각 피자위의 치즈
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 1: 남은 치즈 양, 2: 피자 인덱스
    fire = [C[:N], [i for i in range(N)]]
    # 화덕에 마지막으로 넣은 피자 인덱스
    cnt = N - 1

    # 피자 다 넣을 때까지
    while cnt < M:
        # 화덕 한 바퀴
        for i in range(N):
            fire[0][i] //= 2
            if not fire[0][i]:
                cnt += 1
                if cnt < M:
                    fire[1][i] = cnt
                    fire[0][i] = C[cnt]
    # [[3, 2, 0], [4, 3, 2]]
    # [[2, 8, 7, 1, 0], [6, 7, 8, 9, 4]]
    # [[0, 0, 1, 0, 1], [0, 6, 9, 8, 5]]

    # idx: 치즈가 가장 많이 남은 피자의 화덕에서의 위치
    for i in range(N):
        if fire[0][i]:
            idx = i
            break
    for i in range(1, N):
        if fire[0][i]:
            if fire[0][idx] // 2 < fire[0][i] // 2:
                idx = i
            # 치즈가 가장 많이 남은 피자가 2개면, 먼저 들어온 피자의 위치
            elif fire[0][idx] // 2 == fire[0][i] // 2:
                if fire[1][idx] > fire[1][i]:
                    idx = i

    # 해당 피자의 인덱스
    result = fire[1][idx] + 1
    print('#{} {}'.format(tc, result))