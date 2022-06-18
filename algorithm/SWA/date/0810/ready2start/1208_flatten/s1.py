import sys
sys.stdin = open('input.txt')


# 버블 정렬을 활용하여, 배열 arr를 오름차순 정렬시킨다.
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def flatten(count, heights):
    """
    주어진 덤프 횟수만큼 평탄화를 수행한다.
    count: 덤프 횟수
    heights: 건물들의 높이 (배열)
    """

    # heights 배열을 오름차순 정렬한다.
    bubble_sort(heights)

    for _ in range(count):
        # 최고점과 최저점의 차이가 1 이하라면
        # 평탄화가 이미 완료되었으므로 평탄화를 종료한다.
        if (heights[-1] - heights[0]) <= 1:
            break

        # 최고점의 상자 하나를 최저점에 올려놓는다.
        heights[-1] -= 1
        heights[0] += 1

        # heights의 첫번째, 마지막 값을 다시 정렬시킨다.
        i = 0
        while heights[i] > heights[i + 1]:
            heights[i], heights[i + 1] = heights[i + 1], heights[i]
            i += 1

        j = len(heights) - 1
        while heights[j - 1] > heights[j]:
            heights[j - 1], heights[j] = heights[j], heights[j - 1]
            j -= 1


for tc in range(1, 11):
    dump_count = int(input())
    heights = list(map(int, input().split()))
    # 평탄화 수행
    flatten(dump_count, heights)
    # diff: 최고점과 최저점의 차이
    diff = heights[-1] - heights[0]
    print("#{} {}".format(tc, diff))
