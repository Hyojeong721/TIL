

for i in range(T):
    a, b= map(int, input().split())
    if a > b:
        print('#%d >' %(i))
    elif a < b:
        print('#%d <' %(i))
    else :
        print('#%d =' %(i))