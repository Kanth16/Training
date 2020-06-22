#1
l=["1",2,3,"Hi",1.2,"hello",3.2]
def count(l):
  str1,num,f=[],[],[]
  for i in l:
    if(type(i)==str): str1.append(i)
    elif(type(i)==int): num.append(i)
    else: f.append(i)
  print("String :",str1,"\nInteger:",num,"\nFloat  :",f)
count(l)
#2
q=True
def cont(bool):
  while(bool):
    print("enter any number:")
    n=int(input())
    c=n*n*n
    print("Q/q to exit")
    j=input()
    print("Cube Of",n,":",c)
    if(j.lower()=="q"):bool=False
cont(q)