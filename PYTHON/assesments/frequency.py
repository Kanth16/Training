'''def freq():
    d={}
    string=input()
    for i in string:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
freq()'''

def freq1(name):
    n=list(name)
    n.sort()
    n1=list(set(n))
    for i in range(len(n1)):
        count=0
        for j in range(len(n)):
            if(n1[i]==n[j]):
                count=count+1
                n[j]='0'
        print(n1[i],":",count)
name=input("Enter The Sentence:\n")
freq1(name)