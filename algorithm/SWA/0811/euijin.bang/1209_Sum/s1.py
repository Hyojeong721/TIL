import sys
sys.stdin = open("input.txt")

def findMax(arr):
    '''
    주어진 리스트 아이템 중 최대 값을 구하는 함수

    :return: max value
    '''

    max_value = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

for tc in range(1, 11):
    T = int(input())
    # 100 x 100 이차원 리스트 arr
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행우선순회 통해 각 값들을 리스트에 저장
    rowlist = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        rowlist.append(total)

    # 열우선순회 통해 각 값들을 리스트에 저장
    collist = []
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
        collist.append(total)

    # 대각선순회 통해 각 값들을 리스트에 저장
    diagonallist = []
    total_left = 0
    total_right = 0
    for i in range(100):
        total_left = arr[i][i]
    for i in range(100):
        total_right += arr[i][100 - i - 1]

    diagonallist = [total_left, total_right]

    # 구해진 모든 값을 하나의 리스트에 저장
    total_list = []
    total_list.extend(rowlist)
    total_list.extend(collist)
    total_list.extend(diagonallist)

    print("#{} {}".format(tc, findMax(total_list)))









