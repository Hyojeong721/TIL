import sys
sys.stdin = open('input.txt')

def least_time(routes_info):
    pass
    corridor = [0] * 201
    count = 1
    tmp_left = 0
    tmp_right = 0
    for route in routes_info:
        # (route[0]+1)//2인 이유는 이렇게 해줘야 복도번호가 나옴
        corridor_left = (route[0]+1) // 2
        corridor_right = (route[1]+1) // 2
        if corridor[corridor_left:corridor_right+1] == [0] * (corridor_right - corridor_left + 1):
            corridor[corridor_left:corridor_right+1] = [1] * (corridor_right - corridor_left + 1)
        else:
            for i in range(corridor_left, corridor_right+1):
                if corridor[i] == 1:
                    tmp = i
                    # 1 기준으로 왼쪽을 다 지움
                    while corridor[tmp] == 1:
                        corridor[tmp] = 0
                        tmp -= 1
                    # 오른쪽을 다 지움         전에 담겼던 것을 tmp에 담아서 한번에 지울 수 있을듯
                    while corridor[i+1] == 1:
                        corridor[i+1] = 0
                        i += 1
                break
            count += 1
            corridor[corridor_left:corridor_right + 1] = [1] * (corridor_right - corridor_left + 1)
    return count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 인덱싱을 왼쪽부터 오른쪽으로 할 것이기 때문에 sort해줌
    routes_info = [sorted(list(map(int, input().split()))) for _ in range(N)]
    print('#{} {}'.format(test_case, least_time(routes_info)))