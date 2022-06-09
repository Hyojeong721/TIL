# [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64]

# 구구단 만들기
result = []
for i in range(2, 10):
    dan = []
    for j in range(1, 10):
        if (i % 3 and i % 7 != 0) and (j % 3 and j % 7 != 0):   # 3의 배수와 7의 배수를 제외하고 gugu 에 삽입
            dan.append(i * j)
    result.append(dan)                 # result에 각 단마다 리스트를 만들어 삽입

print(result)
