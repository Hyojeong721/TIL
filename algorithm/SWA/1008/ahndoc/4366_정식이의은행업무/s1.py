import sys
sys.stdin = open('input.txt')

def change_to_dec(num, notation):
    tmp = 0

    # list(map(int, num))[::-1]
    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * notation ** n

    return tmp

def check(num, notation):
    change_num = change_to_dec(num, notation)
    # change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = change_num - val * (notation ** n) + j * (notation ** n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp

T = int(input())
for tc in range(1, T+1):
    bi = input()
    tr = input()

    binary = []
    check(bi, 2)

    print('#{} {}'.format(tc, check(tr, 3)))










# def change2(n):
#     n2_list = []
#     for i in range(len(n)):
#         temp = list(n)
#         if n[i] == '1':
#             temp[i] = '0'
#             n2_list.append(int(''.join(temp)))
#
#         else:
#             temp[i] = '1'
#             n2_list.append(int(''.join(temp)))
#     n2_list = list(set(n2_list))
#     return n2_list
#
# def change3(n):
#     n3_list = []
#     for i in range(len(n)):
#         temp = list(n)
#         if n[i] == '1':
#             temp[i] = '0'
#             n3_list.append(int(''.join(temp)))
#             temp[i] = '2'
#             n3_list.append(int(''.join(temp)))
#
#         elif n[i] == '2':
#             temp[i] = '1'
#             n3_list.append(int(''.join(temp)))
#             temp[i] = '0'
#             n3_list.append(int(''.join(temp)))
#
#         else:
#             temp[i] = '1'
#             n3_list.append(int(''.join(temp)))
#             temp[i] = '2'
#             n3_list.append(int(''.join(temp)))
#     n3_list = list(set(n3_list))
#     return n3_list
#
# def find(arr1, arr2):
#     for i in arr1:
#         for j in arr2:
#             if int(str(i), 2) == int(str(j), 3):
#                 return int(str(i), 2)
#
# T = int(input())
# for tc in range(1, T+1):
#     n2 = list(input())
#     n3 = list(input())
#
#     n2_list = change2(n2)
#     n3_list = change3(n3)
#     ans = find(n2_list, n3_list)
#
#     print('#{} {}'.format(tc, ans))
