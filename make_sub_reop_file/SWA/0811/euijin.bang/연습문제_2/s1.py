import sys
sys.stdin = open("input.txt")

"""
문제: 부분집합의 합
1. 10개의 정수를 입력받는다.
2. 부분집합의 합이 0이 되는 것이 존재하는지 여부를 계산하는 함수를 작성한다.
"""
def isthereSubsetSum0(arr, N):
    """
    부분집합의 합이 0이 되는 것이 존재하는지 여부를 계산하는 함수

    :param arr: 정수 리스트
    :param N: 정수 리스트의 길이
    :return: 존재시 1, 미존재시 0을 반환
    """

    # 공집합을 제외해야 하므로 count 는 -1 부터 시작 (공집합 속의 모든 원소들의 합은 0, 곱은 1로 정의된다.)
    count = -1

    for i in range(1 << N):
        # 1개의 부분집합 아이템의 총합
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += arr[j]
                # print(arr[j], end = ',')
        print()

        # 부분집합의 합이 0이면 개수 추가, 개수가 1 이상이면 true(1) 을 반환
        if total == 0:
            count += 1

    if count > 0:
        return "1"
    else:
        return "0"


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    print("#{} {}".format(tc, isthereSubsetSum0(arr, N)))