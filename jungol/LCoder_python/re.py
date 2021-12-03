# 827
# a = int(input())
# for i in range(1, a+1):
#     print(i, end=' ')

# 828
# num = int(input())
# odd = 0
# even = 0
# while num != 0 :
#     if num % 2: # 홀수
#         odd += 1
#     else:
#         even += 1
#     num = int(input())
#
# print("odd :", odd)
# print("even :", even)

# 829
# num = int(input())
# sum = 0
# cnt = 0
# while 0 <= num <=100:
#     sum += num
#     cnt += 1
#     num = int(input())
# avg = sum/cnt
# print("sum :", sum)
# print("avg : %0.1f" %avg)

# 830
# num = int(input())
# cnt = 0
# while num != 0:
#     if num % 3 == 0 or num % 5 == 0:
#         pass
#     else:
#         cnt += 1
#
#     num = int(input())
# print(cnt)

# 831
# Width = float(input("Width = "))
# Height = float(input("Height = "))
# Triangle_Area = Width * Height / 2
# print("Triangle Area = %0.1f"%Triangle_Area)
# Continue = input("Continue? ")
#
# while Continue == 'Y' or Continue == 'y':
#     Width = float(input("Width = "))
#     Height = float(input("Height = "))
#     Triangle_Area = Width * Height / 2
#     print("Triangle Area = %0.1f" % Triangle_Area)
#     Continue = input("Continue? ")

# 850
# n = int(input())
# for i in range(n):
#     print("JUNGOL")

# 851
# a, b = map(int, input().split())
#
# if a > b :
#     for i in range(b, a+1):
#         print(i, end=' ')
# else:
#     for  j in range(a, b+1):
#         print(j, end=' ')

# 852
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if i % 5 == 0:
#         sum += i
# print(sum)

# 853
# numbers = list(map(int, input().split()))
# # sum = 0
# # for i in numbers:
# #     sum += i
# # avg = sum / len(numbers)
# # print("%0.2f" %avg)

# 854
# numbers = list(map(int, input().split()))
# odd = 0
# even = 0
#
# for num in numbers:
#     if num % 2:
#         odd += 1
#     else:
#         even += 1
# print("even :", even)
# print("odd :", odd)

# 855
# a, b = map(int, input().split())
# sum = 0
# cnt = 0
# if a > b:
#     for i in range(b, a+1):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#             cnt += 1
# else:
#     for i in range(a, b + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#             cnt += 1
#
# avg = sum / cnt
# print('sum :', sum)
# print('avg : %0.1f' %avg)

# 856
# n = int(input())
# for i in range(1, 11):
#     print(n*i, end=' ')

# 857
# a, b = map(int, input().split())
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(j*i, end=' ')
#     print()

# 858
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print((i, j), end=' ')
#     print()

# 859
a, b = map(int, input().split())
if a > b:
    for i in range(1, 10):
        for j in range(a, b-1, -1):
            print(j,"*", i, "=", "{:>2}".format(j*i), end='   ')
        print()
else:
    for i in range(1, 10):
        for j in range(a, b + 1):
            print(j, "*", i, "=", "{:>2}".format(j * i), end='   ')
        print()
