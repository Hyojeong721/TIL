data = [1,2,3,4,5,6,7,8,9,10]
N=len(data)
sel = [0]*N
results = []

def powerset(idx):
    if idx < N:
        sel[idx] = 1

        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

    else:
        total = 0
        for i in range(N):
            if sel[i]==1:
                total+= data[i]

        if total==10:
            for i in range(N):
                if sel[i]==1:
                    print(data[i],end=" ")
            print()
        return

powerset(0)
