import sys
sys.stdin = open('input.txt')

def simple_plus(N, As):
    result = 0
    check = 1
    # 0부터 A개의 개수 - 1 개 만큼
    for i in range(N - 1):
        # 그 다음꺼부터 하나씩 곱한다
        for j in range(i+1, N):
            n = As[i] * As[j]
            # 곱한 수가 단조증가인지 확인
            for k in range(len(str(n)) - 1):
                if int(str(n)[k]) > int(str(n)[k + 1]):
                    check = 0
                    break
            if check and n > result:
                result = n
            check = 1

    if not result:
        result = -1

    return result


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # set 과정을 거쳐 중복 제거
    As = list(set(map(int, input().split())))
    print('#{} {}'.format(test_case, simple_plus(N, As)))