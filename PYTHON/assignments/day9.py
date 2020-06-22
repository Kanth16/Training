def divisible():
  """Multiple of 7 and not a multiple of 5"""
  for i in range(5000,7501):
    if i%7==0 and i%5!=0:
      print(i,end=",")
  print()
def gendrate(n):
  """I/P for List and Tuple of the comma separated String"""
  l1=n.split(",")
  print(l1)
  print(tuple(l1))
def fibonacci():
  """fibonacci series till 200"""
  a,b,c=0,1,0
  while(c<201):
    c=a+b
    a=b
    b=c
    print(a,end=",")