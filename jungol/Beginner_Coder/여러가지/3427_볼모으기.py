n = int(input())
balls = input()

# 한종류로만 주어질 때
if balls.count(balls[0]) == len(balls):
    print(0)

first = balls[-1]
if first == 'B':
    second = 'R'
else:
    second = 'B'

# 오른쪽으로 해당 색깔 볼을 모으는 경우
same_idx = n-1
while first:
    if balls[same_idx] == first:
        same_idx -= 1
    else:
        break
first_right = balls[:same_idx+1]
second_right = balls
first_right_cnt = first_right.count(first)
second_right_cnt = second_right.count(second)

# 왼쪽으로 해당 색상 볼을 모으는 경우
first = balls[0]
if first == 'B':
    second = 'R'
else:
    second = 'B'

same_idx = 0
while first:
    if balls[same_idx] == first:
        same_idx += 1
    else:
        break
first_left = balls[same_idx+1:]
second_left = balls
first_left_cnt = first_left.count(first)
second_left_cnt = second_left.count(second)

res = min(first_right_cnt, first_left_cnt, second_right_cnt, second_left_cnt)
print(res)
