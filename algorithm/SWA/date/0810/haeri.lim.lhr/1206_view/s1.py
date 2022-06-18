import sys
sys.stdin = open('input.txt')

# 조망권을 확인하는 함수 view 선언
def view(width, apart):

    #기준 빌딩의 각 왼쪽 빌딩과의 조망권과 오른쪽 빌딩과의 조망권을 저장하는 변수 선언
    left_temp, right_temp = 0, 0

    # 기준 빌딩의 왼쪽 빌딩과의 층수 차이와 두번째 왼쪽 층수 차이를 저장하는 변수 선언
    # 기준 빌딩의 오른쪽 빌딩과의 층수 차이와 두번째 오른쪽 층수 차이를 저장하는 변수 선언
    left_fist, left_second, right_fist, right_second = 0, 0, 0, 0

    # 모든 빌딩의 조망권이 좋은 층수의 총합을 저장하는 변수 total 선언
    total = 0
    # 건물마다 조망권이 좋은 층수를 저장하는 배열 result 선언
    result = [0] * width

    # 건물마다 조망권을 알아보는 반복문 시행
    for i in range(2, width-2):

        # 기준 빌딩과 첫번째 왼쪽 아파트와 두번째 왼쪽 아파트 차이
        left_fist = apart[i] - apart[i-1]
        left_second = apart[i] - apart[i-2]

        # 만약 전부 양의 정수라면 더 작은 값을 왼쪽 조망권 층수로 저장
        # 아니라면 0으로 저장
        if left_fist > 0 and left_second > 0 and left_fist >= left_second:
            left_temp = left_second
        elif left_fist > 0 and left_second > 0 and left_second >= left_fist:
            left_temp = left_fist
        else:
            left_temp = 0

        # 기준 빌딩과 첫번째 오른쪽 아파트와 두번째 오른쪽 아파트 차이
        right_fist = apart[i] - apart[i + 1]
        right_second = apart[i] - apart[i + 2]

        # 만약 전부 양의 정수라면 더 작은 값을 오른쪽 조망권 층수로 저장
        # 아니라면 0으로 저장
        if right_fist > 0 and right_second > 0 and right_fist >= right_second:
            right_temp = right_second
        elif right_fist > 0 and right_second > 0 and right_fist >= right_fist:
            right_temp = right_fist
        else:
            right_temp = 0

        # 왼쪽 조망권 층수와 오른쪽 조망권 층수중에서 더 작은 값으로 result 배열에 저장
        if right_temp == 0 or left_temp == 0:
            result[i] = 0
        elif right_temp >= left_temp:
            result[i] = left_temp
        elif left_temp >= right_temp:
            result[i] = right_temp


    # result 배열에 저장된 층수의 총합
    for j in result:
        total += j

    return total

# 가로 길이 width 선언
# 빌딩 데이터 apart 선언
for test_case in range(1,11):
    width = int(input())
    apart = list(map(int, input().split()))
    print('#%d %d'%(test_case, view(width, apart)))