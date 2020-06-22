def sumofdigits(str):
  a=0
  for i in str:
    if(i.isdigit()):a=a+int(i)
  print(a)
def ispalindrome(str):
  a=str[::-1]
  if a==str:print("Palindrome")
  else:print("Not Palindrome")
def binary(bin):
  print(int(bin,2))