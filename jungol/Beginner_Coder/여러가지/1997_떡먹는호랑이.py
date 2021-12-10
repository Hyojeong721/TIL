d, k = map(int, input().split())

# k = (d-3)*a + (d-1)*b
for a in range(1, k):
    if (k - ((d-3)*a)) % (d-1) == 0:
        b = (k - ((d - 3) * a)) // (d - 1)

        if a <= b < a+b and k == ((d-3)*a) + ((d-1)*b):
            before = a+b
            for i in range(4, d+1):
                if before > ((i-3)*a) + ((i-1)*b):
                    break
                else:
                    if i == d+1:
                        print(a, b)

