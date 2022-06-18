import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # K: 1회 급유시 이동 가능 거리/ N: 종착점 번호/ M: gas station 개수
    gas = list(map(int, input().split()))

    cnt = 0  # gas station 방문 횟수
    now = 0  # 현재 정거장
    possible = 0  # 이전에 방문 가능했던 gas station 개수(방문 log)

    while now < N:
        possible_stop = [x for x in gas if x <= now + K]  # 현재 위치에서 방문 가능한 gas station 목록
        if gas[0] > K:  # 출발점에서 처음 gas staion까지 갈 수 없는 경우
            print(f'#{tc} 0')  # '0출력'
            break
        elif len(possible_stop) == possible:  # 방문 가능한 gas station 목록이 업데이트 안되는 경우
            print(f'#{tc} 0')  # '0출력'
            break
        elif len(possible_stop) != possible:  # 방문 가능한 gas station 목록이 업데이트 된 경우
            cnt += 1  # 방문 횟수를 증가시키고
            possible = len(possible_stop)  # 이전 방문 log를 업데이트
            now = possible_stop[-1]  # 현재 위치를 최대 도달 가능한 gas station으로 이동
            if now + K >= N:  # 만약 마지막 gas station에서의 급유로 종착점까지 갈 수 있는 경우, while문 break
                print(f'#{tc} {cnt}')
                break