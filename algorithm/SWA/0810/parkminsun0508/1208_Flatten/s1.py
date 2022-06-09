# swea 1208 Flatten
# 평탄화 작업 후 최고점과 최저점의 차이를 반환
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    # 덤프 횟수와 상자위치 리스트를 받는다.
    dump = int(input())
    num_list = list(map(int, input().split()))
    # 덤프 횟수를 소진하여 0이 될 때까지 반복한다.
    while dump > 0:
        num_max = num_list[0]
        num_min = num_list[0]
        # 모든 박스 높이를 비교하며 최대, 최소값을 할당한다.
        for num in num_list:
            if num > num_max:
                num_max = num
            if num < num_min:
                num_min = num
        for j in range(len(num_list)):
            # 반복문 중 박스 높이가 최댓값과 같다면 그 줄의 상자를 하나 제거한다.
            if num_list[j] == num_max:
                num_list[j] -= 1
                # 박스 높이가 최솟값과 같으면 상자를 하나 추가한다.
                for i in range(len(num_list)):
                    if num_list[i] == num_min:
                        num_list[i] += 1
                        break
                break
        # 상자가 이동하기에 덤프 횟수가 하나 소진되었다.
        dump -= 1
    # 초기화 후 할당한다.
    num_max = num_list[0]
    num_min = num_list[0]
    # 상자 높이를 모두 비교하며 최대, 최소 값 할당한다.
    for num in num_list:
        if num >= num_max:
            num_max = num
        if num <= num_min:
            num_min = num
    print('#{} {}'.format(tc, num_max-num_min))