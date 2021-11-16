import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    n = int(input())
    tmp_nums = list(map(int, input().split()))
    nums = tmp_nums[::-1] + [0]   # list 순서 뒤집고 마지막에 0 추가
    # print(nums)


    stack = [nums[0]]   # 초기값 설정
    buy = []   # 매수한 물건의 가격 리스트
    prof = 0   # 지금까지의 이익
    idx = 1    # index

    while idx < len(nums):   # nums의 모든 항목 탐색
        v = stack[-1]        # stack의 마지막 값 호출

        if nums[idx] > v or nums[idx] == 0:  # 현재값이 stack값보다 크거나 탐색 종료시
            for b in buy:                    # 지금까지 매수한 물건의 이익 계산 후 합산
                prof += v - b                # profit에 추가
            buy = []
            stack.append(nums[idx])          # 현재값을 stack에 추가

        else:                          # 현재값이 stack값보다 작은 경우
            buy.append(nums[idx])      # 물건의 가격을 buy에 추가
        # print(idx, v, nums[idx], buy, prof)
        idx += 1

    print('#{} {}'.format(t, prof))