import sys
sys.stdin = open('input.txt')

def least_time(routes_info):
    pass
    corridor = [0] * 201
    count = 1
    for route in routes_info:
        # (route[0]+1)//2인 이유는 이렇게 해줘야 복도번호가 나옴
        corridor_left = (route[0]+1) // 2
        corridor_right = (route[1]+1) // 2
        if corridor[corridor_left:corridor_right+1] == [0] * (corridor_right - corridor_left + 1):
            corridor[corridor_left:corridor_right+1] = [1] * (corridor_right - corridor_left + 1)
        else:
            # 사용중이었던 복도를 모두 찾아 0으로 바꿔주고 카운트를 1 추가해주려 했으나매우 귀찮음

            count += 1
            corridor[corridor_left:corridor_right + 1] = [1] * (corridor_right - corridor_left + 1)

    return count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 인덱싱을 왼쪽부터 오른쪽으로 할 것이기 때문에 sort해줌
    routes_info = [sorted(list(map(int, input().split()))) for _ in range(N)]
    print('#{} {}'.format(test_case, least_time(routes_info)))