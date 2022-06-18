import sys
sys.stdin = open('input.txt')

T = int(input())

# 개수를 반환하는 함수 count_str 선언
def count_str(str1, str2):
    # 빈 딕셔너리 result 선언
    result = {}

    # str1의 요소와 str2의 요소가 같을 경우 count 추가
    # i 값을 key로 count를 value로 딕셔너리 저장
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        result[i] = count

    max_value = 0

    # 딕셔너리에서 가장 큰 값 찾아서 반환
    for key, value in result.items():
        if value > max_value:
            max_value = value

    return max_value



for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print('#%d %s' %(test_case, count_str(str1, str2)))