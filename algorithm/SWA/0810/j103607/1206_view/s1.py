import sys
sys.stdin = open('input.txt')



TC = 10
for tc in range(1, TC+1):
    # 총 건물 수
    N = int(input())
    # 건물 높이 리스트
    area = list(map(int, input().split()))

    total = 0
    for i in range(2, N-2): # i = 2~97

        # first = i-2 < i < i+2 범위에서 제일 높은 건물
        first = 0
        small_range = area[i-2:i+3]
        for f in small_range:
            if first <= f:
                first = f

        # second = i-2 < i < i+2 범위에서 두번째 높은 건물
        small_range.remove(first)

        second = small_range[0]
        for s in small_range:
            if second <= s:
                second = s

        # i가 small range[i-2, i-1,  i, i+1, i+2] 범위에서 제일 높은 건물(first)이랑 같으면 second와의 차를 total에 더하기
        if area[i] == first:
            diff = area[i] - second
            total += diff

    print('#{} {}'.format(tc, total))