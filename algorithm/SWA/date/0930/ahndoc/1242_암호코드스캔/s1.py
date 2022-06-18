import sys
sys.stdin = open('input.txt')
"""
코드가 존재하는 열을 찾는다
16진수 -> 2진수
글자수 잘라주기

0의 의미 : 1) 빈공간, 2) 패턴

맨 앞의 0은 무시해도 됨
3:1:1:2
0 1 0 1
뒷부분부터 카운팅해주자 
나눠주자
first = 0 
second = 0
third = 0
"""
# dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
#
# cnt_p = [[3, 2, 1, 1],
#         [2, 2, 2, 1],
#         [2, 1, 2, 2],
#         [1, 4, 1, 1],
#         [1, 1, 3, 2],
#         [1, 2, 3, 1],
#         [1, 1, 1, 4],
#         [1, 3, 1, 2],
#         [1, 2, 1, 3],
#         [3, 1, 1, 2]
#          ]
#
# def change(n):
#     result = ''
#     for i in n:
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         result = ''
#         if i.isdigit():
#             t = format(int(i), 'b')
#             if len(t) != 4:
#                 while len(t) != 4:
#                     t = '0' + t
#             result += t
#         else:
#             result += format(dic[i], 'b')
#     return result
#
#
# def calc(p):
#     odd = 0
#     even = 0
#     for i in range(4):
#         odd += p[i*2]
#         even += p[i*2+1]
#     if (odd * 3 + even) % 10 == 0:
#         return sum(p)
#     return 0
#
# def patterns_count(first, second, third):
#     v = min(first, second, third)
#     first //= v
#     second //= v
#     third //= v
#     fourth = 7 - (first + second + third)
#     return [fourth, third, second, first]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(input() for _ in range(N))
#     arr = list(set(arr))
#     patterns = []
#     for i in range(len(arr)):
#         temp = ''
#         for j in range(M):
#             temp += change(arr[i][j])
#         patterns.append(temp)
#
#     # for data in arr:
#     #     if data.count('0') != len(data):
#     #         temp = ''
#     #         for i in data:
#     #             temp += change(i)
#     #         patterns.append(temp)
#
#     my_patterns = []
#     for pattern in patterns:
#         my_patterns.append(pattern.rstrip('0'))
#
#     ans = 0
#     solved_patterns = []
#     visited = []
#     for pattern in my_patterns:
#
#         first = 0
#         second = 0
#         third = 0
#
#         for i in range(len(pattern)-1, -1, -1):
#             if not second and pattern[i] == '1':
#                 first += 1
#
#             elif first and not third and pattern[i] == '0':
#                 second += 1
#
#             elif second and pattern[i] == '1':
#                 third += 1
#
#             if first and second and third and pattern[i] == '0':
#                 tmp = patterns_count(first, second, third)
#
#                 first = 0
#                 second = 0
#                 third = 0
#
#                 for j in range(10):
#                     if cnt_p[j] == tmp:
#                         solved_patterns.append(j)
#                         break
#
#                 if len(solved_patterns) == 8:
#                     solved_patterns = solved_patterns[::-1]
#                     a = calc(solved_patterns)
#
#                     if a and solved_patterns not in visited:
#                         ans += a
#                         visited.append(solved_patterns)
#
#                     solved_patterns = []
#     print('#{} {}'.format(tc, ans))

pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}


def find():
    ans = 0
    for i in range(N):  # 세로의길이가 N이라서
        idx = len(arr) - 1  # 마지막 인덱스
        # idx = M * 4 - 1

        while idx >= 55:
            if arr[i][idx] and arr[i - 1][idx] == 0:
                pwd = []
                for _ in range(8):
                    # 뒤에서부터 1 카운트 0카운트 1 카운트를 각각 c4 c3 c2에 저장함.
                    c2 = c3 = c4 = 0
                    # 처음 나오는 0들을 버리자.
                    while arr[i][idx] == 0: idx -= 1
                    while arr[i][idx] == 1: c4, idx = c4 + 1, idx - 1  # 1을 만났으면 1을 카운트
                    while arr[i][idx] == 0: c3, idx = c3 + 1, idx - 1  # 0을 만났으면 카운팅
                    while arr[i][idx] == 1: c2, idx = c2 + 1, idx - 1  # 1을 만났으면 카운팅
                    min_value = min(c2, c3, c4)
                    pwd.append(pattern[(c2 // min_value, c3 // min_value, c4 // min_value)])

                b = pwd[0] + pwd[2] + pwd[4] + pwd[6]  # 짝수번쨰 자리임.
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (a * 3 + b) % 10 == 0:
                    ans += a + b

            idx -= 1

    return ans


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로의길이, M 가로의길이
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hexTobin[tmp[j]]
    # 전부 2진수로 바꿨당~~~

    print("#{} {}".format(tc, find()))