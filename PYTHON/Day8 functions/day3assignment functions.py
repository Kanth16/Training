s='I drink coffee every morning'
s1='I like python ,Perl scripting'
name="Kanthimathinathan Ramasubramanian"
spaces=": vect1 and vect2 are lists of equal length of numbers"
str1 = "PYnative"
def coffee(s):
  print("'coffee' in s:",'coffee' in s)
def flname(name):
  name1=name.split(" ")
  print("name :",name1[0]+"."+name1[1][0])
def bspaces(spaces):
  print(spaces.count(" "))
def slicing(str1):
  l1=s1.split(" ")[3].split(",")[1]
  print(l1[0])
  print(str1[1:4]+" "+str1[:5]+" "+str1[4:]+" "+str1[:7]+" "+str1[:7])
coffee(s)
flname(name)
bspaces(spaces)
slicing(str1)