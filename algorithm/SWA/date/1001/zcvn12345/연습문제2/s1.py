def Perm(arr, n, k):
    if k == n:
        a = arr[:]
        num_lst.append(a)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            Perm(arr, n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

def BabyGin(n):
    if n[0] == n[1]-1 and n[1] == n[2]-1:
        return True
    elif n[0] == n[1] == n[2]:
        return True
    else:
        return False


num_lst = []
Perm([6,6,7,7,6,7], 6, 0)
# num_lst = list(set(num_lst))
result = False
for i in num_lst:
    a = i[:3]
    b = i[3:]
    if BabyGin(a) and BabyGin(b):
        result =True
        break
print(result)