n = int(input())
minhuck = [list(map(int, input().split())) for _ in range(n)]
# minhuck = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

numbers = [i for i in range(111, 1000)]
temp = [i for i in range(111, 1000)]
def strike(vs_num, stan):
    global num
    strike_cnt = 0
    for i in range(3):
        if vs_num[i] == stan[i]:
            strike_cnt += 1

    return strike_cnt

def ball(num, stan):
    ball_cnt = 0
    stan_lst = list(stan)
    for i in range(3):
        if num[i] == stan[i]:
            stan_lst[i] = 0
    for i in range(3):
        if num[i] in stan_lst:
            ball_cnt += 1
    return ball_cnt
def same_num(num):
    global numbers
    for i in range(3):
        if num.count(num[i]) > 1:
            numbers.remove(int(num))
            break
    return

for number in temp:
    num = str(number)
    for m in minhuck:
        standard = str(m[0])
        stan_str = m[1]
        stan_bal = m[2]
        res_str = strike(num, standard)
        res_bal = ball(num, standard)
        if '0' in num and number in numbers:
            numbers.remove(number)
            break
        if stan_str != res_str or stan_bal != res_bal:
            if number in numbers:
                numbers.remove(number)
                break
        if number in numbers:
            same_num(num)

print(len(numbers))
