n=int(input())
l=[-4,-3,1,6,-7,0,9,-1,5]
def table(n):
  for i in range(1,n+1): print("7 X",i,"=",7*i)
def count(l):
  nc=pc=0
  for i in l:
    if i<0:nc=nc+1
    else:pc=pc+1
  print(l)
  print("-ve count :",nc)
  print("+ve count :",pc)
table(n)
count(l)