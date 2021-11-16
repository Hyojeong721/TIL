import time
Arr = [i for i in range(1, 100)]

N = len(Arr)

checked = [0] * N
result = []
RS = sum(Arr)
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

def powerset(idx, s, t, RS):
    global num1, num2, num3, num4, num5, N

    if s > t:
        num1 += 1
        return

    if RS == 0:
        num5 += 1
        return

    elif s + RS < t:
        num2 += 1
        return

    elif idx == N:
        num3 += 1
        return

    elif s == t:
        num4 += 1
        for i in range(N):
            if checked[i]:
                print(Arr[i], end = ' ')
        print()
        return



    checked[idx] = 1
    powerset(idx + 1, s + Arr[idx], t, RS - Arr[idx])

    checked[idx] = 0
    powerset(idx + 1, s, t, RS - Arr[idx])

A = []
# for i in range(5):
a = time.time()
powerset(0, 0, 60, RS)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(time.time() - a)
# print(sum(A)/5)

#없을때 4.8 평균
#있을때 5.12