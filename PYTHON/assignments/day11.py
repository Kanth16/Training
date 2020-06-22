#1
def callfuc(a,b):
    return a+b
a=int(input())
b=int(input())
if(b==0):
    print("Invalid value")
else:
    print(callfuc(a,b))
#2
def  swap(name):
    a=[]
    for i in name:
        j=ord(i)
        if j >= 97 and j <= 122: a.append(chr(j-32))
        elif j >= 65 and j <= 90: a.append(chr(j+32))
    return a
name=input()
name1=swap(name)
print("".join(name1))
#3
def _abecedarian(name):
    for i in range(1,len(name)):
        if (name[i-1] == chr(ord(name[i])-1) or name[i]==name[i-1] and ord(name[i])<=ord(name[i-1])):
            return True
    return False
name=input().lower()
print(_abecedarian(name))
#4
def convert(deg):
    if("F" in deg):
        a=int(deg.replace("F",""))
        c=(a-32)*(5/9)
        print(deg,c,"C")
    elif("C" in deg):
        a=int(deg.replace("C",""))
        f=(a*1.8)+32
        print(deg,f,"F")
deg=input("Temp. Convertion: \n").upper()
convert(deg)