# swea 4835 구간 합
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
import sys
sys.stdin = open('input.txt')
# 먼저, 테스트 케이스의 수를 받는다.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 정수 리스트를 받아온다.
    num_list = list(map(int, input().split()))

    # 리스트 안에 값을 넣어 보여준다.
    result = []
    # max-min을 하여 결과를 나타낸다.
    answer = []

    # 범위가 index 값을 벗어나지 않도록 N에서 M을 빼준다.
    for i in range(N-M+1):
        result.append(sum(num_list[i:i+M]))
    # result의 최대에서 최소를 빼준다.
    answer = max(result) - min(result)
    print('#{} {}'.format(tc, answer))



