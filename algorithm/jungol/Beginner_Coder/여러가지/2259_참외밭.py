k = int(input())
field = [list(map(int, input().split())) for _ in range(6)]
max_garo = 0
max_sero = 0

for i in range(6):
    if field[i][0] == 1 or field[i][0] == 2:
        if max_garo < field[i][1]:
            max_garo = field[i][1]
            max_garo_idx = i
    if field[i][0] == 3 or field[i][0] == 4:
        if max_sero < field[i][1]:
            max_sero = field[i][1]
            max_sero_idx = i

if max_garo_idx+1 > 5:
    res_sero = abs(field[max_garo_idx - 1][1] - field[0][1])
else:
    res_sero = abs(field[max_garo_idx - 1][1] - field[max_garo_idx + 1][1])

if max_sero_idx+1 > 5:
    res_garo = abs(field[max_sero_idx - 1][1] - field[0][1])
else:
    res_garo = abs(field[max_sero_idx - 1][1] - field[max_sero_idx + 1][1])

res = (max_garo * max_sero) - (res_garo * res_sero)
print(res * k)