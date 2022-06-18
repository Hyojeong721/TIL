import sys
sys.stdin = open('input.txt')

# 선택정렬을 이용해 작은 수부터 정렬
def list_sort(num_list):
    for i in range(0, len(num_list)-1):
        min = i
        for j in range(i+1, len(num_list)):
            if num_list[min] > num_list[j]:
                min = j
        num_list[i], num_list[min] = num_list[min], num_list[i]
    return num_list


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = list_sort(numbers)

    # 정렬된 리스트에서 큰수(맨 마지막) -> 작은수(맨 앞) 번갈아가면서 result에 저장
    result = []
    for i in range(5):
        result.append(sorted_numbers[len(sorted_numbers)-1-i])
        result.append(sorted_numbers[i])

    result = ' '.join(list(map(str, result)))

    print('#{} {}'.format(tc, result))