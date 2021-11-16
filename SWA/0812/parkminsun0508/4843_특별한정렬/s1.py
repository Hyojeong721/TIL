# 4843 특별한 정렬
import sys
sys.stdin = open("input.txt")

# 선택정렬로 큰값, 작은값 가져오는 함수 정의하기
def selecsort(arr):
    for i in range(len(arr)-1):
        get_min = i
        for j in range(i+1, len(arr)):
            if arr[get_min] > arr[j]:
                get_min = j
        arr[i], arr[get_min] = arr[get_min], arr[i]

# 테스트 케이스 개수를 받아온다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr_list = list(map(int, input().split()))
    selecsort(arr_list)
    result = []
    # 총 10개 결과 반환해야하며 리스트 2개씩 5쌍이기에 range 5
    for i in range(5):
        result += [arr_list[N-1-i]]
        result += [arr_list[i]]

    print('#%d ' % t, end='')
    print(*result)
