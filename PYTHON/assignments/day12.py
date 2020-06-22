#1
def _issorted(l):
    '''***LIST***'''
    a=l.copy()
    a.sort()
    if(a==l): return True
    else:return False
print(_issorted.__doc__)
n=int(input())
l=[]
for i in range(n):
    l.append(input())
print(_issorted(l))

#2
class check_name:
    '''***CLASS***'''
    def _lower(self,name):
        l=[]
        for i in name:
            if(ord(i)>=ord("a") and ord(i)<=ord("z")):l.append(i)
        print(l)
    def _upper(self,name):
        l=[]
        for i in name:
            if(ord(i)>=ord("A") and ord(i)<=ord("Z")):l.append(i)
        print(l)
    def _split(self,name):
        l=[]
        l=name.split(" ")
        print(l)
    def _vowel(self,name):
        l=[]
        for i in name:
            a=i.lower()
            if(i in ["a","e","i","o","u"]):l.append(i)
        print(l)
cn=check_name()
print(check_name.__doc__)
name=input("Enter name")
cn._lower(name)
cn._upper(name)
cn._split(name)
cn._vowel(name)