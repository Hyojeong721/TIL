# baby gin
import random
numbers = [random.choice(range(0, 10)) for _ in range(6)]
print(numbers)


def run(arr):
    if arr == list(range(arr[0], arr[0]+3)):
        return 1
    else:
        return 0


def triplet(arr):
    if arr == [arr[0]]*3:
        return 1
    else:
        return 0


def baby_gin(n, k):
    if k == n:
        permutations.append(numbers)
    else:
        for i in range(k, n):
            numbers[k], numbers[i] = numbers[i], numbers[k]
            baby_gin(n, k+1)
            numbers[k], numbers[i] = numbers[i], numbers[k]


permutations = []
baby_gin(6, 0)


for permutation in permutations:
    cnt = 0
    cnt += run(permutation[0:3]) + triplet(permutation[0:3])
    cnt += run(permutation[3:6]) + triplet(permutation[3:6])
    if cnt == 2:
        print('baby-gin')
        break
else:
    print('lose')





