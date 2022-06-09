import sys
sys.stdin = open('input.txt')

def get_overlapping_area(N, boxes, M=10):
    """
    red 와 blue 가 겹친 purple 영역의 넓이를 반환하는 함수
    N: 칠할 영역의 개수 (constant)
    boxes: 각 칠할 영역의 인덱스와 색칠정보 (list)
    M: 격자 길이

    """
    # red 로 칠할 격자
    mat_red = [[0] * M for _ in range(M)]
    cnt = 0

    # red box 와 blue box 의 index 를 개별 리스트로 저장
    red_box_index = []
    blue_box_index = []
    for idx, box in enumerate(boxes):
        if box[-1] == 1:
            red_box_index.append(idx)
        else:
            blue_box_index.append(idx)

    # mat_red 내에 red box 들이 있는 영역에 +1
    for red_box in red_box_index:
        start = [boxes[red_box][0], boxes[red_box][1]]
        end = [boxes[red_box][2], boxes[red_box][3]]
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                mat_red[i][j] += 1

    # mat_red 에 색칠되어 있는 부분이 blue box와 겹친다면 cnt +1
    for blue_box in blue_box_index:
        start = [boxes[blue_box][0], boxes[blue_box][1]]
        end = [boxes[blue_box][2], boxes[blue_box][3]]
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if mat_red[i][j] > 0:
                    cnt += 1

    # 겹친 넓이 반환
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    boxes = []
    for _ in range(N):
        boxes.append(list(map(int, input().split())))
    area = get_overlapping_area(N, boxes)
    print('#{0} {1}'.format(tc, area))