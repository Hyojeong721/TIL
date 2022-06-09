import sys
sys.stdin = open('input.txt')

# test case 개수
T = int(input())

# 가장 많은 카드의 숫자와 장 수를 차례로 출력
def get_major_card(nums):
    counts = [0] * 10
    for num in nums:
        counts[int(num)] += 1

    major = 0
    for i in range(10):
        if counts[major] <= counts[i]:
            major = i

    return major, counts[major]


# 모든 test case 마다 실행
for t in range(1, T + 1):
    N = int(input())
    nums = input()
    major_card, major_num = get_major_card(nums)
    print('#{0} {1} {2}'.format(t, major_card, major_num))

