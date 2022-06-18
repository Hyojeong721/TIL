import sys
sys.stdin = open('input.txt')

# 왼쪽 위 모서리 = r1, c1, \
# 오른쪽 아래  모서리 = r2, c2
# color = 1(빨강), color = 2(파랑)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 첫 줄에 칠할 영역의 개수 = N
    total = 0
    red_set = set()
    blue_set = set()
    for i in range(N):
        arr = list(map(int, input().split()))  # 한줄씩 인풋된다.
        # 시작 인덱스(r1, c1) 끝 인덱스(r2, c2)
        r1, c1 = arr[0], arr[1]
        r2, c2 = arr[2], arr[3]

        # 색상에 따라 포인트지점을 각 색상 set에 입력
        if arr[4] == 1:
            for r1 in range(r1, r2 + 1):
                c1 = arr[1]
                for c1 in range(c1, c2 + 1):
                    red_set.add((r1, c1))

        elif arr[4] == 2:
            for r1 in range(r1, r2 + 1):
                c1 = arr[1]
                for c1 in range(c1, c2 + 1):
                    blue_set.add((r1, c1))

        # red와 blue 영역 중 겹치는 영역 갯수
        for red in red_set:
            for blue in blue_set:
                if red == blue:
                    total += 1

    print('#{} {}'.format(tc, total))

# set을 쓴 이유는 같은 색 영역에서 두번 들어가서 겹치는 영역 갯수에
# 중복이 생길까봐 그런건데 문제에서 보면 같은색은 겹치는 영역이 없다라고
# 제한해주었다. => 결론. 문제를 정확히 제대로 읽자.