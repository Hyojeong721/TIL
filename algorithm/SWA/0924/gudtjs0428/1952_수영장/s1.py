import sys
sys.stdin = open('input.txt')

def lowest_cost(tickets, schedule):
    day_fee, month_fee, three_m_fee, year_fee = tickets[0], tickets[1], tickets[2], tickets[3]
    price_per_month = [0] * 12
    price = 0
    for i in range(12):
        days = schedule[i]
        if days * day_fee > month_fee:
            price_per_month[i] = month_fee
        else:
            price_per_month[i] = days * day_fee
    for i in range(10):
        tmp = []
        price_three_month = sum(price_per_month[i:i+3])
        if price_three_month > three_m_fee:
            tmp.append([i, price_three_month])

        # price_per_month[i:i+3] = [0, 0, three_m_fee]
    if sum(price_per_month) + price > year_fee:
        price = year_fee
    else:

        price = sum(price_per_month)
    return price




T = int(input())
for test_case in range(1, T + 1):
    tickets = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    print('#{} {}'.format(test_case, lowest_cost(tickets, schedule)))