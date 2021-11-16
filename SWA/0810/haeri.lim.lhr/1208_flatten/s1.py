import sys
sys.stdin =open('input.txt')

# 평탄화 시키는 함수 dump 선언
def dump(dump_count, box):
    # 덤프 시킨 횟수를 저장하는 count 선언
    count = 0

    # 최대 dump_count만큼 반복 시행
    while count < dump_count:
        # 가장 박스가 많은 값 max_box, 적은 값 min_box
        max_box = max(box)
        min_box = min(box)

        # 각각의 값에 해당하는 인덱스 max_box_index, min_box_index
        max_box_index = box.index(max_box)
        min_box_index = box.index(min_box)

        # 해당 인덱스의 값 변경
        box[max_box_index] -= 1
        box[min_box_index] += 1

        # 덤프 시행 횟수 1 추가
        count += 1

        # 덤프 시행 후 최대값과 최소값의 차이 result 저장
        result = max(box) - min(box)

        # 만약 dump_count전 평탄화 완료시 반복문 탈출
        if result == 0 or result == 1:
            return result

    return result

# 덤프 제한 횟수 dump_count 선언
# 박스 갯수 box 선언
for test_case in range(1, 11):
    dump_count = int(input())
    box = list(map(int, input().split()))
    print('#%d %d' %(test_case, dump(dump_count, box)))