import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,1+T):
    N = int(input())
    temp =[]
    temp.extend(str(input()))
    matrix = []

    for i in temp:
        card_count = temp.count(i)
        matrix.append([i,card_count])

    result = matrix[0]
    card = matrix[0][1]

    for j in matrix:
        if j[1] > card:
            card = j[1]
            result = j
        elif j[1] == card:
            if int(j[0]) >= int(result[0]):
                result = j

    print('#%d %s %d' %(test_case, result[0], result[1]))