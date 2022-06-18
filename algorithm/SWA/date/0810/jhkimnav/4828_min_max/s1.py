import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    list_numbers = list(map(int, input().split()))

    # 최대값과 최솟값을 찾기 위한 두 변수인
    # max_value와 min_value에 주어진 리스트의 첫 번째 원소로 초기화
    max_value = list_numbers[0]
    min_value = max_value

    for i in range(1, len(list_numbers)):

        # 최대값인지 검사
        if max_value < list_numbers[i]:
            max_value = list_numbers[i]

        # 최소값인지 검사
        if min_value > list_numbers[i]:
            min_value = list_numbers[i]

    # 결과 값인 최대값 - 최소값 출력
    print('#{} {}'.format(test_case, max_value - min_value))

