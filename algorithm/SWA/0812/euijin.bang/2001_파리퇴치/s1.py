import sys
sys.stdin = open("input.txt")


def singleTryNum(arr, M, row, col):
    """
    M * M 크기 파리채로 매 시도에서 죽 파리의 수를 반환하는 함수

    arr = N * N 배열
    M : 파리채 가로 or 세로
    :return: 죽은 파리의 수
    """
    count = 0

    for i in range(M):
        for j in range(M):
            count += arr[i+row][j+col]
    return count


def everyTryList(arr, N, M):
    """
    N * N 배열에서 각 시도별 죽인 파리수를 리스트로 반환하는 함수

    :return: 시도별 죽은 파리 수가 담긴 리스트
    """
    trial = []
    for row in range(N-(M-1)):
        for col in range(N-(M-1)):
            trial.append(singleTryNum(arr, M, row, col))
    return trial


def findMax(arr):
    """
    정수 리스트에서 최대 아이템을 반환하는 함수

    :param arr: 정수 리스트
    :return: max
    """
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val



T = int(input())

for tc in range(1, T+1):
    # N * N 배열
    # M * M 파리채의 크기
    N, M = map(int, input().split())

    # arr : 이중 배열, 이차원 리스트
    arr = [list(map(int, input().split()))for _ in range(N)]

    ans = findMax(everyTryList(arr, N, M))
    print("#{} {}".format(tc, ans))