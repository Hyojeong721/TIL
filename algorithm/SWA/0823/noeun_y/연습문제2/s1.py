arr = ['하나','둘','셋']
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(len(sel)):
            if sel[i]:
                print(arr[i],end="")
        print("")
        return


    sel[idx]=0
    powerset(idx+1)

    sel[idx]=1
    powerset(idx+1)


powerset(0)


