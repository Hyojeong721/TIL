import sys
sys.stdin = open('input.txt')
# 조망권이 확보된 세대의 수를 반환하는 프로그램
# 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        # 왼쪽 조망권 and 오른쪽 조망권
        if 0 <= i - 2 < N and 0 <= i + 2 < N:
            left_max = arr[i-2]
            right_max = arr[i+2]
            # 왼쪽, 오른쪽에서 높은 건물 선택
            if left_max < arr[i-1]:
                left_max = arr[i-1]
            if right_max < arr[i + 1]:
                right_max = arr[i+1]

            building = left_max
            # 왼쪽과 오른쪽 높은건물중 누가 더 높은지
            if left_max < right_max:
                building = right_max

            # 조망권 보장 되는지 확인
            if arr[i]-left_max >= 0 and arr[i]-right_max >= 0:
                cnt += arr[i] - building

    print("#{} {}".format(tc, cnt))

# 자꾸 헷갈렸던 부분 -> 조망권 보장되는지 확인하는부분에서
# 0이상이면 되는데 자꾸 2이상이면 된다고 했었다.


