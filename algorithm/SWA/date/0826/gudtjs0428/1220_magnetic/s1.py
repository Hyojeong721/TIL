import sys
sys.stdin = open('input.txt')

# state 대박

def count_deadlocks(magnetics):
    count = 0
    for i in range(100):
        deadlocks = []

        for j in range(100):
            if magnetics[j][i] == 1:
                if not deadlocks or (deadlocks and deadlocks[-1] == 1):
                    deadlocks.append(1)
                elif deadlocks and deadlocks[-1] == 2:
                    deadlocks = [1]
                    count += 1
            elif magnetics[j][i] == 2 and deadlocks:
                deadlocks.append(2)
        if deadlocks and deadlocks[-1] == 2:
            count += 1

    return count

T = 10
for test_case in range(1, T + 1):
    input()
    magnetics = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(test_case, count_deadlocks(magnetics)))