import sys
sys.stdin = open('input.txt')
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#
#     1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#     2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#     3. 판매는 얼마든지 할 수 있다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[-1]
    result = 0

    # 반대로 생각하기
    for n in range(N-1, -1, -1):
        # 현재 최댓값 구하기 / 지금이 더 최대면 아무짓안함.
        if max_value <= arr[n]:
            max_value = arr[n]
        # 지금이 더 작은 값이라면 사서 미래에 판다!
        else:
            # 시세차익 계산
            result += max_value - arr[n]

    print("#{} {}".format(tc, result))
