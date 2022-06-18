import sys
sys.stdin = open('input.txt')
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
N = int(input())


def my_max(numbers):
    my_max = numbers[0]
    for i in range(len(numbers)-1):
        if my_max < numbers[i+1]:
            my_max = numbers[i+1]
    return my_max

def my_min(numbers):
    my_min = numbers[0]
    for i in range(len(numbers)-1):
        if my_min > numbers[i+1]:
            my_min = numbers[i+1]
    return my_min

for number in range(N):
    case_number ='#'+str(number+1)
    case = int(input()) #5
    numbers = list(map(int, input().split()))
    result = my_max(numbers) - my_min(numbers)
    print(case_number, result)












