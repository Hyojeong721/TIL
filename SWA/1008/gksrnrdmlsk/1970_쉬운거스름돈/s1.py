import sys
sys.stdin = open('input.txt')
tenders = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    lst = []
    for i in tenders:
        lst.append(str(money // i))
        money %= i
    print('#{}'.format(tc))
    print(' '.join(lst))

# for tc in range(1, T + 1):
#     money = int(input())
#     lst = []
#     for i in tenders:
#         if i != 10:
#             lst.append(money // i)
#             money = money % i
#         else:
#             if money % 10:
#                 lst.append((money // i) + 1)
#             else:
#                 lst.append(money // i)
#     print('# {}'.format(tc))
#     for i in lst:
#         print(i, end=' ')
#     print()
