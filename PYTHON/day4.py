name=input("Enter the string")
if(name==name[::-1] and len(name)!=0):
  print("palindrome")
else:
  print("not a palindrome")
l=[1,2,3,4,5,6,7,8,9,10]
print([i*10 for i in l if(i*10)%50==0])