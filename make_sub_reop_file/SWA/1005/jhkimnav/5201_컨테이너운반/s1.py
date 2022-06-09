import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 컨테이너 수
    # M : 트럭 수
    N, M = map(int, input().split())
    contain_list = sorted(list(map(int, input().split())))
    truct_list = sorted(list(map(int, input().split())))

    print('컨테이너 : {}'.format(contain_list))
    print('트럭 : {}'.format(truct_list))
    answer = 0

    for i in range(min(N, M)):
        if truct_list[-1] >= contain_list[-1]:
            answer += contain_list[-1]
            truct_list.pop()
            contain_list.pop()
        else:
            contain_list.pop()
        # print('컨테이너 : {}'.format(N_list))
        # print('트럭 : {}'.format(M_list))
    print('#{} {}'.format(tc, answer))
