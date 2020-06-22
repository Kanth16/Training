#Merge Dictonary and OrderedDict
from collections import OrderedDict
s={'a':1,'b':2,'c':3}
s1={'d':4,'e':5,'f':6}
s1.update(s)
print(s1)
print(OrderedDict(s1.items()))
#1
s=input()
def sumofdigits(s):
  a=0
  for i in s:
    if(i.isdigit()):a=a+int(i)
  print(a)
sumofdigits(s)
#2
s=input()
def ispalindrome(str):
  a=s[::-1]
  if a==s:print("Palindrome")
  else:print("Not Palindrome")
ispalindrome(s.input())
#3
def binary(bin):
  print(int(bin,2))
binary('10011')