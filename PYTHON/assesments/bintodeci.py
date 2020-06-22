def bindec(a,b):
    s=int(a+b)
    i=num=0
    while(s>0):
        num=num+(s%10)*(2**i)
        s=int(s/10)
        i=i+1
    print(num)
a,b=input("Enter 2 binary values:\n"),input()
bindec(a,b)