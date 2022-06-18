import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    # 0~N까지 각 자리에서 요소값보다 작은거 갯수
    for i in range(N):
        number = arr[i]
        min_list = []
        # 본인보다 작은 요소들 list에 담기
        for j in range(i+1, N):
            if number > arr[j]:
                min_list.append(arr[j])
        # 가장 큰 갯수를 가진 리스트의 길이를 결과값으로 저장한다.
        if result < len(min_list):
            result = len(min_list)

    print('#{} {}'.format(tc, result))