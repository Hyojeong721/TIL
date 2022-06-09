import sys
sys.stdin = open('input.txt')

N = int(input())

def get_max(size_of_matrix, matrix):
    max_num = 0
    result = []
    for i in range(size_of_matrix):
        for j in range(i+1, size_of_matrix):
            if matrix[i] <= matrix[j]:
                max_num = j - i
                result.append(max_num)
                break
    return max(result)

for test in range(N):
    size_of_matrix = int(input())
    matrix = list(map(int, input().split()))
    print(get_max(size_of_matrix, matrix))
