import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = []
    for num in input():
        numbers.append(int(num))
    count = [0] * 10

    for idx, value in enumerate(count):
        for number in numbers:
            if number == idx:
                value += 1

    print(count)



    # max = 0
    # for item in count:
    #     if max < count[item]:
    #         max = count[item]
    #
    # for key in count.keys():
    #     if int(key)
    #
    # for key, value in count.items():
    #     if value == max:
    #         print('#{0} {1} {2}'.format(i, key, value))
