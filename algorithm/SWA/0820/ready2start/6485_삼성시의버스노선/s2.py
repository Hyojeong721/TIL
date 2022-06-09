# 강의를 보고 다시 작성한 풀이 (훨씬 효율적)

import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # starts: 각 버스 정류장에서 출발하는 버스의 개수
    # ends: 각 버스 정류장에서 멈추는 버스의 개수
    starts = [0] * 5001
    ends = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        starts[A] += 1
        ends[B] += 1

    # bus_counts: 각 버스 정류장을 지나는 버스의 개수를 저장한 배열
    bus_counts = [0] * 5001

    """
    n번 정류장을 지나는 버스의 개수
    = (n - 1)번 정류장을 지나는 버스의 개수
        + n번 정류장에서 출발하는 버스의 개수
        - (n - 1)번 정류장에서 멈추는 버스의 개수
    """
    for i in range(1, 5001):
        bus_counts[i] = bus_counts[i - 1] + starts[i] - ends[i - 1]

    P = int(input())

    print("#{}".format(tc), end=" ")

    for _ in range(P):
        C = int(input())
        print(bus_counts[C], end=" ")
    print()
