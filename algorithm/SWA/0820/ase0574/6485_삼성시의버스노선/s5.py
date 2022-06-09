# 0824 _ runtime error _ 수정
import sys
sys.stdin = open('input.txt')

T = int(input())

def bus_cnt(C):
    cnt = 0

    for i in range(N):
        if bus[i][0] <= C <= bus[i][1]:
            cnt += 1
    return cnt


for tc in range(1, T+1):
    N = int(input()) # 버스 노선 수
    # 버스 다니는 정류장 (시작점, 끝점)
    bus = [list(map(int, input().split())) for _ in range(N)]
    # 확인 정류장 수
    P = int(input())
    # 정류장마다 지나는 버스 갯수 저장리스트
    result = []

    for i in range(P):
        C = int(input())
        result.append(bus_cnt(C))
        # result[C] += bus_cnt(c) 안되는 이유
        # 확인할 정류장의 번호가 1,5,7,9이런식이면 출력할때 슬라이싱으로 안됌
        # 그래서 궁금한 정류장 번호의 노선 순서대로 그냥 넣고 전체출력해야함.


    print('#{}'.format(tc), end=' ')
    print(*result)

