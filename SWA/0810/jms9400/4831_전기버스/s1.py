import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    K, N, M = list(map(int, input().split())) # K : 최대이동 정류장수, N : 종점 정류장, M : 충전기 정류장 수
    stop = list(map(int, input().split()))
    charge = 0
    location = 0
    temp_break = 0

    while location < N - K: #for문 말고 while 문으로
        location += K
        print(location)
        if location in stop:
            charge += 1
        else:
            for j in range(location-1, location-K, -1):
                if j in stop:
                    charge += 1
                    location = j
                    break
            else:
                temp_break = 1
                print('#{} 0'.format(test_case))
                break

    if temp_break == 1:
        pass
    else:
        print('#{} {}'.format(test_case, charge))