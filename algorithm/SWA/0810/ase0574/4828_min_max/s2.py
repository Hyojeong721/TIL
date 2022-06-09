import sys
sys.stdin = open('input.txt')
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_number = arr[0]
    min_number = arr[0]
    for i in range(N):
        if max_number < arr[i]:
            max_number = arr[i]
        elif min_number > arr[i]:
            min_number = arr[i]
    result = max_number - min_number
    print('#{} {}'.format(tc,result))