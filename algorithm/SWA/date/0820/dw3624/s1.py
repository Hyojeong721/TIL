# baby-gin
num = 456789
c = [0] * 12

# 각 자릿수를 배열에 저장
for i in range(6):
    c[num % 10] += 1
    num //= 10
print(c)

i = 0
tri = run = 0
while i < 10:
    print(c[i])
    if c[i] >= 3:  # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')