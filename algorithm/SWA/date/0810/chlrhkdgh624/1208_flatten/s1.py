import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())  # 이동 가능 횟수
    boxes = list(map(int, input().split()))  # 박스들의 배치
    while dump > 0:
        high = max(boxes)  # 가장 높은 층
        low = min(boxes)  # 가장 낮은 층
        boxes[boxes.index(high)] -= 1  # 가장 높은 층 - 1
        boxes[boxes.index(low)] += 1  # 가장 낮은 층 + 1
        dump -= 1  # 이동 가능 횟수 감소
        if high - low <= 1:  # 가장 높은 층과 낮은 층의 차이가 1 이하이면 break
            break

    print(f'#{tc} {max(boxes)-min(boxes)}')
