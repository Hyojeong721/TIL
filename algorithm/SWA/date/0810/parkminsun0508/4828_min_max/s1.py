# swea 4828 min_max
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
import sys
sys.stdin = open('input.txt')
# 먼저, 테스트 케이스의 수를 받는다.
T = int(input())
# 각 테스트 케이스마다 반복하여 확인한다.
for c in range(1, T+1):
    # 각 케이스의 첫 줄에 주어진 양수의 개수를 받아, 리스트로 만든다.
    N = int(input())
    N_list = list(map(int, input().split()))
    # min, max 초기설정
    N_min = N_list[0]
    N_max = N_list[0]
    # 주어진 양수 리스트의 각 인자들에 대해 for 반목문으로 돌며 최소값, 최대값을 만든다.
    for num in N_list:
        if num < N_min:
            N_min = num
        if num > N_max:
            N_max = num
    print('#{} {}'.format(c, N_max - N_min))
    # 출력예시에 각 케이스별 max - min 이 적혀있기 때문에
    # print(N_max - N_min) 이렇게 하면 값만 나올 뿐 케이스 별 번호가 나오지 않는다.

