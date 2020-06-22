class matrix:
    def __init__(self):
        l1,l2=[],[]
        try:
            print("enter matrix dimensions:(N X N)")
            n,m=int(input()),int(input())
            print("Enter Elements:")
            for i in range(n):
                a=[]
                for j in range(m):
                    a.append(int(input("Matrix1:")))
                l1.append(a)
            for i in range(n):
                a=[]
                for j in range(m):
                    a.append(int(input("Matrix2:")))
                l2.append(a)
            for i in range(n):
                for j in range(m):
                    print(l1[i][j],end=" ")
                print()
            print()
            for i in range(n):
                for j in range(m):
                    print(l2[i][j],end=" ")
                print()  
            print("enter Operations:(+,-,X)")
            op=input()
            if op =="+":self.add(n,m,l1,l2)
            elif op=="-": self.sub(n,m,l1,l2)
            elif op=="X" or op=="x":self.mul(n,m,l1,l2)
            else:print("wrong input")
        except ValueError:
            print("Enter the values properly")
    def add(self,n,m,l1,l2):
        addi=[]
        for i in range(n):
            a=[]
            for j in range(m):
                a.append(l1[i][j]+l2[i][j])
            addi.append(a)
        for i in range(n):
            for j in range(m):
                print(addi[i][j],end=" ")
            print()
    def sub(self,n,m,l1,l2):
        subr=[]
        for i in range(n):
            a=[]
            for j in range(m):
                a.append(l1[i][j]-l2[i][j])
            subr.append(a)
        for i in range(n):
            for j in range(m):
                print(subr[i][j],end=" ")
            print()
    def mul(self,n,m,l1,l2):
        mult=[]
        for i in range(n):
            a=[]
            for j in range(m):
                sum=0
                for k in range(n):
                    sum=sum+(l1[i][k]*l2[k][j])
                a.append(sum)
            mult.append(a)
        for i in range(n):
            for j in range(m):
                print(mult[i][j],end=" ")
            print()
obj=matrix()