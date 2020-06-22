name=input()
a=[]
a=name.split(" ")
for i in range(len(a)):
  asc=ord(a[i][0])
  if(asc>=97 and asc<=122):
    a[i]="".join(a[i].replace(a[i][0],chr(asc-32)))
print("".join(a))