import sys
sys.stdin = open('input.txt')

T = int(input())

def paper_recursive(width_digit):
    """
    (20 X l) 크기의 교실 바닥이 주어졌을 때
    (10 x 20) 타일과 (20 X 20) 타일로
    바닥을 모두 채우는 경우의 수

    width : 교실 바닥의 가로길이
    Returns: 타일로 교실 바닥을 채우는 경우의 수
    """

    if width_digit == 1:
        return 1
    elif width_digit == 2:
        return 3
    else:
        return paper_recursive(width_digit-1) + 2*paper_recursive(width_digit-2)

for tc in range(1, T+1):
    N = int(input())
    width_digit = N // 10
    result = paper_recursive(width_digit)
    print ('#{} {}'.format(tc, result))
