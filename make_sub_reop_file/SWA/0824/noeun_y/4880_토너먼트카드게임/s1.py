import sys
sys.stdin =open('input.txt')

def whowin(a,b):

    if card[a-1]==card[b-1]:
        return a

    elif card[a-1]==1:
        if card[b-1]==2:
            return b
        elif card[b-1]==3:
            return a
    elif card[a-1]==2:
        if card[b-1]==3:
            return b
        elif card[b-1]==1:
            return a
    elif card[a-1]==3:
        if card[b-1]==1:
            return b
        elif card[b-1]==2:
            return a


def halfcut(a,b):
    if a == b:
        return a
    elif b-a ==1:
        return whowin(a,b)

    else:
        mid=(a+b)//2
        return whowin(halfcut(a,mid),halfcut(mid+1,b))




for tc in range(1,int(input())+1):

    N = int(input())
    card = list(map(int,input().split()))
    #print(card)
    print("#{} {}".format(tc,halfcut(1,N)))