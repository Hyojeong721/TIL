a = int(input())
b = int(input())
c = int(input())
# a = 150
# b = 266
# c = 427
# 100 <= a, b, c < 1000
# A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하기.

result = a * b * c
str_result = str(result)
arr = [0]*10

for i in str_result:
    for j in range(10):
        if int(i) == j:
            arr[j] += 1

for k in arr:
    print(k)