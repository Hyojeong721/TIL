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
# a, b = map(int, input().split())
# if a > b:
#     for i in range(1, 10):
#         for j in range(a, b-1, -1):
#             print(j,"*", i, "=", "{:>2}".format(j*i), end='   ')
#         print()
# else:
#     for i in range(1, 10):
#         for j in range(a, b + 1):
#             print(j, "*", i, "=", "{:>2}".format(j * i), end='   ')
#         print()

# 869
# i = 48
# while i <= 90:
#     print(i, '-', chr(i))
#     i += 1

# 870
# n = int(input())
# i = n+96
# # 97 = a / 122 = z
# # 1 -> +96
#
# while 97 <= i <= 122:
#     print(chr(i), end='')
#     i += n

# 871
# n = int(input())
# for i in range(1, n+1):
#     print('*'*i)
#
# for j in range(n-1, 0, -1):
#     print('*'*j)

# 872
# n = int(input())
# for j in range(n-1, 0, -1):
#     str = '*'*(j*2+1)
#     print(str.center((n-1)*2+1))
#
# for i in range(n):
#     str = '*'*(i*2+1)
#     print(str.center((n-1)*2+1))

# 873
# n = int(input())
#
# for i in range(n):
#     str = '*'*(i*2+1)
#     print(str.rjust((n-1)*2+1))


# 874
# n = int(input())
#
# for i in range(1, n+1):
#     ans = ''
#     for j in range(1, i+1):
#         if j == i:
#             ans = ans + str(j)
#         else:
#             ans = ans + str(j) + ' '
#     print(ans.rjust(2*n-1))

# 875
# n = 3
# cnt = 65
# ans = [([0]*n) for _ in range(n)]
# for i in range(n):
#     for j in range(n-i):
#         ans[i][j] = chr(cnt)
#         cnt += 1
# num = 0
# for k in range(n):
#     for l in range(n):
#         if type(ans[k][l]) == int:
#             ans[k][l] = num
#             num += 1
#         if l == n-1:
#             print(ans[k][l])
#         else:
#             print(ans[k][l], end=' ')

# 876
# n = 4
# cnt = 1
# ent = ''
# for i in range(n):# 총 n줄
#     print(ent, end='')
#     ent += '  '
#
#     for j in range(n-i):
#         if j == n-i-1:
#             print(cnt, end='')
#             cnt += 1
#         else:
#             print(cnt, end=' ')
#             cnt += 1
#     print()

# 877
# n = 4
# for i in range(1, n+1):
#     print('# '*i)
#
# for j in range(n-1, 0, -1):
#     print('  '*(n-j)+'# '*j)

# 878
n = 3
cnt = 1
for i in range(n):
    for j in range(n):
        if cnt <= 5:
            print(cnt*2-1, end=' ')
        else:
            cnt = 1
            print(cnt*2-1, end=' ')
        cnt += 1
    print()