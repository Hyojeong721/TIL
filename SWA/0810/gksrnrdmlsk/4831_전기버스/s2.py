# 재귀로 풀기
import sys
sys.stdin = open('input.txt')

T = int(input()) # 몇 번의 테스트 케이스가 있을지 입력받습니다.

def charger(lst, stp, count):
    if stp >= N - K:
        return count
    for j in range(stp + K, stp, -1):  # 최소한으로 충전하기 위해 큰 숫자부터 range를 구성합니다.
        if j in lst:  # 갈 수 있는 충전소 중 가장 멀리 있는 충전소를 찾습니다.
            return charger(lst, j, count+1)
    return 0

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    print('#{0} {1}'.format(tc, charger(lst, 0, 0)))
