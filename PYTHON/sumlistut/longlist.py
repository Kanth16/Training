def llist(num,n):
    a=[int(i) for i in num]
    b=[]
    for i in range(0,len(a)):
        sums=0
        counter=[]
        for j in range(i,len(a)):
           sums=sums+a[j]
           if(sums==n):
            counter.append(a[j])
            b.append(counter)
            break
           elif(sums>n):
            del counter[-1]
            sums=sums-n
           else:
            counter.append(a[j])
    a=[len(i) for i in b]
    return(max(a))