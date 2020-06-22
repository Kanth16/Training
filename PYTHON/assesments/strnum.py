def strnum(word):
    f=0
    for i in word:
        if i.isdigit():
            print(i,end="")
            f=1
    if f==0:
        print("No numbers")
word=input()
strnum(word)