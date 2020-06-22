class moper:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return b-a
    def div(self,a,b):
        return b/a
    def mod(self,a,b):
        return b%a
oj=moper()
a=int(input())
b=int(input())
print("+",oj.add(a,b))
print("-",oj.sub(a,b))
print("/",oj.div(a,b))
print("%",oj.mod(a,b))