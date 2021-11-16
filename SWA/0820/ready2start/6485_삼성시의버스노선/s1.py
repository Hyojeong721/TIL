import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # bus_counts: 각 버스 정류장에 지나는 버스 노선의 개수를 저장한 배열
    bus_counts = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        # A에서 B까지의 버스 노선의 개수에 1씩 더한다.
        for i in range(A, B + 1):
            bus_counts[i] += 1

    P = int(input())

    print("#{}".format(tc), end=" ")

    for _ in range(P):
        C = int(input())
        print(bus_counts[C], end=" ")
    print()
