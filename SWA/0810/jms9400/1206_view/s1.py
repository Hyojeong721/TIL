import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    max_num = 0
    second_num = 0
    result = 0

    for i in range(0, n-4):

        temp_list = building[i:i+5]

        for temp in temp_list:
            if temp >= max_num:
                max_num = temp

        if max_num == building[i+2]:
            for j in range(5):
                if j == 2:
                    pass
                elif building[i+j] >= second_num:
                    second_num = building[i+j]
            result += max_num - second_num
            second_num = 0
        max_num = 0


    print('#{} {}'.format(tc, result))









# def get_max(size_of_matrix, matrix):
#     max_num = 0
#     result = []
#     for i in range(size_of_matrix):
#         for j in range(i+1, size_of_matrix):
#             if matrix[i] <= matrix[j]:
#                 max_num = j - i
#                 result.append(max_num)
#                 break
#     return max(result)
#
# for test in range(N):
#     size_of_matrix = int(input())
#     matrix = list(map(int, input().split()))
#     print(get_max(size_of_matrix, matrix))