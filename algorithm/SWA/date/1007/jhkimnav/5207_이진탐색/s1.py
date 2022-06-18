import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 탐색해야할 리스트
    N_list = sorted(list(map(int, input().split())))
    
    # 탐색할 Key 값이 들은 리스트
    M_list = list(map(int, input().split()))
    
    cnt = 0

    # M_list 를 차례대로 key 값에 넣고
    for i in range(M):
        key = M_list[i]
        l = 0
        r = N - 1
        # 이전에 탐색한 영역을 검증하기 위한 문자열
        check = ''

        # 왼쪽을 가리키는 l idx가 r 보다 왼쪽에 있는 경우는 계속 탐색 진행
        while l <= r:
            mid = (l + r) // 2
            if N_list[mid] == key:
                cnt += 1
                break
            
            # mid 값이 키 값보다 큰 경우
            # 왼쪽 구간 선택
            elif N_list[mid] > key:
                r = mid - 1
                now = 'left'
            
            # mid 값이 키 값보다 작은 경우
            # 오른쪽 구간 선택
            else:
                l = mid + 1
                now = 'right'

            if check == now:
                break

            check = now

    print('#{} {}'.format(tc, cnt))

