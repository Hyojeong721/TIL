import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    """
    방 전체를 1차원 배열로 생각함.
    예를 들어, room1과 room2는 모두 1차원 배열의 0번 인덱스라고 생각함.
    
    starts: 이동 경로의 왼쪽 끝 위치를 저장하는 배열
            (ex. starts[2]가 2라면, room3이나 room4에서 출발하거나 도착하는 경로가 2개)
    ends: 이동 경로의 오른쪽 끝 위치를 저장하는 배열
    visited: 위치별 방문 횟수를 저장하는 배열
    """
    starts = [0] * 201
    ends = [0] * 201
    visited = [0] * 201

    for _ in range(N):
        num1, num2 = map(int, input().split())

        # num2가 더 크다면 num1이 왼쪽 끝, num2가 오른쪽 끝이다.
        if num1 < num2:
            starts[(num1 + 1) // 2] += 1
            ends[(num2 + 1) // 2] += 1
        # num1이 더 크다면 num2가 왼쪽 끝, num1이 오른쪽 끝이다.
        else:
            starts[(num2 + 1) // 2] += 1
            ends[(num1 + 1) // 2] += 1

    # 초기값 설정 (0번째 인덱스를 중간에 거쳐가는 경우는 없음.)
    visited[0] = starts[0] + ends[0]

    """
    i번째 인덱스를 지나는 이동 경로 수 
        = (i - 1)번째 인덱스를 지나는 이동 경로 수
          + i번째 인덱스를 왼쪽 끝으로 가지는 이동 경로 수
          - (i - 1)번째 인덱스를 오른쪽 끝으로 가지는 이동 경로 수                                   
    """
    for i in range(1, 201):
        visited[i] = visited[i - 1] + starts[i] - ends[i - 1]

    max_visit = 0
    for x in visited:
        if x > max_visit:
            max_visit = x

    print("#{} {}".format(tc, max_visit))
