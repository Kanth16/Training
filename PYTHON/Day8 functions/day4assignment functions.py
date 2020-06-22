#1 number cone
print("#1")
a=int(input())
def cone(a):
  for i in range(a,0,-1):
    for j in range(i):
      print(i,end="")
    print()
cone(a)
#2 odd/even count
def oddeven():
  print("#2")
  oc=ec=0
  for i in range(533875):
    if i % 2==0: ec=ec+1 
    else: oc=oc+1
  print("Odd count :",oc,"\n"+"Even count:",ec)
oddeven()
#3 Credit Card Validity
print("#3")
n = int(input())
def credit(n):
  l,b=[],[]
  counter = 0
  out=1
  for i in range(n):
      a = input()
      l.append(a)
  for i in range(n):
      out=1
      flag = 0
      if ("-" in l[i]):
          b = l[i].split("-")
          l[i] = "".join(b)
          for j in range(len(b)):
              if (len(b[j]) != 4 and len(b)==4):out=0
      if(l[i][0]=="4" or l[i][0]=="5" or l[i][0]=="6"):
          if (len(l[i]) == 16 and out!=0):
            if (l[i].isdigit()):
                  if ("$" not in l[i] or "@" not in l[i] or "#" not in l[i]  or "%" not in l[i] or "&" not in l[i]):
                      for k in range(1,len(l[i])):
                          if (l[i][k-1] == l[i][k]):
                              counter = counter + 1
                              if (counter >= 4):flag = 1
                          else: counter = 0
                  else: flag=1
          else: flag=1
      else: flag=1
      if (flag == 0): print("Valid")
      else:print("InValid")
credit(n)