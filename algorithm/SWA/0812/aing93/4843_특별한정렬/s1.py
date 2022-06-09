import sys
sys.stdin = open('input.txt')

T = int(input())

# 버블정렬 함수
def bubble_sort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(0,i):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 버블정렬 함수
    numbers = bubble_sort(numbers)
    result = []
    # 정렬된 숫자 10개를 5까지 순회하면서 뒤에서 하나, 앞에서 하나씩 뽑기
    for i in range(5):
        # 정렬된 리스트의 맨 마지막, 즉 가장 큰값 먼저 추출
        result.append(numbers[len(numbers)-1-i])
        # 다음으로 리스트의 맨 앞, 즉 가장 작은값 추출
        result.append(numbers[i])
    # 공백으로 숫자 구분
    result = ' '.join(map(str, result))
    print("#{} {}".format(tc, result))


