def maxi1(l):
    b=[str(i) for i in l]
    b="".join(b)
    b=b.split("0")
    return len(max(b))
    #print(max(b))
#max1([1,1,1,0,0,1,0,1,1,0])
#max1([1,1,1,0,1,1,1,1,1,0,0,1,1,0,0])