import sys
sys.stdin = open('input.txt')

# tc가 10개
for tc in range(1, 11):

    # tc의 길이
    n = int(input())

    # 빌딩의 높이
    heights = list(map(int, input().split()))

    # 조망권 확보 수
    cnt = 0

    # 확인 위치
    idx = 2

    # 마지막 오른쪽 2개는 0 0 이므로 확인 안 해도 됨
    while idx < n - 2:

        # 왼쪽에 있는 것들보다 작으면 idx 한 칸 이동, 한 칸 오른쪽 옆에 있는 빌딩보다 작으면 한 칸 이동
        if heights[idx] <= heights[idx - 2] or heights[idx] <= heights[idx - 1] or heights[idx] <= heights[idx + 1]:
            idx += 1
            pass

        # 두 칸 오른쪽 옆에 있는 빌딩보다 작으면 두 칸 이동
        elif heights[idx] <= heights[idx + 2]:
            idx += 2
            pass

        # 조망권이 확보 된 경우
        else:

            # 조망권 확보 숫자 더해주기
            cnt += heights[idx] - max(heights[idx - 2], heights[idx - 1], heights[idx + 1], heights[idx + 2])

            # 오른쪽으로 3칸 이동
            idx += 3

    print('#{} {}'.format(tc, cnt))