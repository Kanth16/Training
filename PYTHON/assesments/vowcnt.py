import collections
def vowcnt(string):
    l=string.split(" ")
    d={}
    #l1=[]
    for i in l:
        count=0
        for j in range(len(i)):
            if i[j] in ["a","e","i","o","u"]:
                count=count+1
      #  l1.append((count,i))
    #l1.sort()
    #print(l1)
        d[count]=i
    d=collections.OrderedDict(sorted(d.items()))
    print(d)
string=input()
vowcnt(string)