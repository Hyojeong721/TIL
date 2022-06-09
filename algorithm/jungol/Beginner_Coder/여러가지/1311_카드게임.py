color = []
numbers = []
score = 0
for n in range(5):
    col, num = input().split()
    color.append(col)
    numbers.append(int(num))

numbers.sort()
num_dic = {}
for number in numbers:
    if number in list(num_dic.keys()):
        num_dic[number] += 1
    else:
        num_dic[number] = 1

values = list(num_dic.values())
values.sort()
num_cnt = len(values)

# 규칙 1
if color.count(color[0]) == 5:
    f = numbers[0]
    if [f, f+1, f+2, f+3, f+4] == numbers:
        score = 900 + max(numbers)
    # 규칙 4
    else:
        score = 600 + max(numbers)

if score == 0:
    score_temp = score
    # 규칙 5
    if num_cnt == 5:
        f = list(num_dic.keys())[0]
        if [f, f+1, f+2, f+3, f+4] == list(num_dic.keys()):
            score = f + 4 + 500
    # 규칙 8
    elif num_cnt == 4:
        for key, val in num_dic.items():
            if val == 2:
                score = key + 200
    elif num_cnt == 3:
        temp = []
        for key, val in num_dic.items():
            # 규칙 6
            if val == 3:
                score = key + 400
                break
            # 규칙 7
            if val == 2:
                temp.append(key)
        if temp:
            temp.sort()
            score = 10 * temp[-1] + temp[0] + 300

    elif num_cnt == 2:
        score = 0
        # 규칙 2 : 동일 숫자 4개, 1개
        for key, val in num_dic.items():
            if val == 4:
                score = 800 + key
                break
            # 규칙 3: 동일 숫자 3개, 2개
            elif val == 3:
                score += key*10
            elif val == 2:
                score += key + 700

    if score_temp > score:
        score = score_temp

if score == 0:
    score = max(numbers) + 100

print(score)