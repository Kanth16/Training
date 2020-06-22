def count(l):
  str1,num,f=[],[],[]
  for i in l:
    if(type(i)==str): str1.append(i)
    elif(type(i)==int): num.append(i)
    else: f.append(i)
  print("String :",str1,"\nInteger:",num,"\nFloat  :",f)
def cont(bool):
  while(bool):
    print("enter any number:")
    n=int(input())
    c=n*n*n
    print("Q/q to exit")
    j=input()
    print("Cube Of",n,":",c)
    if(j.lower()=="q"):bool=False