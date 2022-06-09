# 781
# lst = ['Salad', 'Pizza', 'Chicken', 'Soup']
# print(lst)

# 782
# lst = ['Python', 'is', 'exciting']
# for i in lst:
#     print(i, end=' ')

# 783
# list_1 = [1, 2, 3]
# list_2 = [2, 4, 6]
# list_3 = [3, 6, 9]
#
# print(list_1 + list_3*3 + list_2)

# 784
# lst = [1, 2]
# # num = int(input())
# # lst.append(num)
# # lst.reverse()
# # for i in lst:
# #     print(i)

# 785
# str = input()
# print(str[0])
# print(str[2])

# 786
# arr = []
# for i in range(6):
#     str = input('Element? ')
#     arr.append(str)
# idx = int(input('Index? '))
# print(arr[idx::])

# 787
# arr_f = []
# arr_s = []
# for i in range(1, 7):
#     str = input('Element? ')
#     if i % 2:
#         arr_f.append(str)
#     else:
#         arr_s.append(str)
#
# print(arr_f + arr_s)

# 788
# nums = [i for i in range(1, 16)]
# user = int(input())
# ans = []
# for i in nums:
#     if i % user == 0:
#         ans.append(i)
# print(ans)

# 789
# str = list(input().split())
# print(str[::-1])

# 790
# minus = [i for i in range(-1, -6, -1)]
# print(minus)

# 791
# lst_f = input().split()
# lst_s = input().split()
#
# ans_f = [int(lst_f[0]) for _ in range(int(lst_f[1]))]
# ans_s = [int(lst_s[0]) for _ in range(int(lst_s[1]))]
# print(ans_f + ans_s)

# 792
# color = []
# animal = []
# for i in range(4):
#     user = input('Input? ').split()
#     color.append(user[0])
#     animal.append(user[1])
# print('Color:', color)
# print('Animal:', animal)

# 793
# user = list(input())
# print(user[::-1])

# 794
# lst = list(input().split())
# ans = []
# for i in range(1, len(lst)+1):
#     if i%3 == 0:
#         ans.append(str(lst[i-1]))
# print(ans)

# 795
lst = input().split()
print(lst[-2:0:-1])

