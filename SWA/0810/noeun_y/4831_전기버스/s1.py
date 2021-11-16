for tc in range(1,int(input())+1):
        K,N,M = map(int,input().split())
        stoplist = list(map(int,input().split()))       
        stoplist.sort(reverse=True)
        pre = 0
        count=0
        while pre+K<N:
            if {i for i in range(pre,pre+K+1)} & set(stoplist):
                pre=stoplist.pop(stoplist.index(max({i for i in range(pre,pre+K+1)} & set(stoplist))))                    
            else:
                count=0
                break
            count+=1
        print("#{} {}".format(tc,count))