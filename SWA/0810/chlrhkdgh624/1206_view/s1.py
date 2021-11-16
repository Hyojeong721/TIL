import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    view = 0
    width = int(input())
    heights = list(map(int, input().split()))

    for i in range(2, width-2):
        if heights[i] != max(heights[i-2:i+3]):  # [i-2, i-1, i , i +1, i +2]
            continue
        else: # i번째 건물이 가장 높은 건물
            viewpoint = [x - heights[i] for x in heights[i-2:i+3]]  # [0, 0, 5, 4, 3] 각 요소에 가운데 건물 높이 빼줌
            viewpoint.remove(0)
            view -= max(viewpoint)

    print(f'#{tc} {view}')
