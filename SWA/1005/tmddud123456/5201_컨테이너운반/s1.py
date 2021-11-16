import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    container, truck = list(map(int, input().split()))
    container_list = sorted(list(map(int, input().split())), reverse=True)
    truck_list = sorted(list(map(int, input().split())), reverse=True)
    i = 0
    total = 0
    for truck_1 in truck_list:
        for n in range(i, len(container_list)):
            if truck_1 >= container_list[n]:
                total += container_list[n]
                i = n+1
                break
    print('#{} {}'.format(tc, total))