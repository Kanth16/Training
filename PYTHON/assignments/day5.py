n=int(input())
for i in range(1,n+1): print("7 X",i,"=",7*i)
nc=pc=0
l=[-4,-3,1,6,-7,0,9,-1,5]
for i in l:
  if i<0:
    nc=nc+1
  else:
    pc=pc+1
print("-ve count :",nc)
print("+ve count :",pc)