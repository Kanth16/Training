import day3assignmentmodules
import day4assignmentmodules
import day5assignmentmodules
import day6assignmentmodules
import day7assignmentmodules
import day8assignmentmodules
import count
s=input("Count of cases\n")
count.cases(s)
s='I drink coffee every morning'
s1='I like python ,Perl scripting'
name="Kanthimathinathan Ramasubramanian"
spaces=": vect1 and vect2 are lists of equal length of numbers"
str1 = "PYnative"
print("Day 3")
day3assignmentmodules.coffee(s)
day3assignmentmodules.flname(name)
day3assignmentmodules.sl(s1)
day3assignmentmodules.bspaces(spaces)
day3assignmentmodules.slicing(str1)
print("Day 4")
print("cone")
a=int(input())
day4assignmentmodules.cone(a)
day4assignmentmodules.oddeven()
print("Credit Card")
n=int(input())
day4assignmentmodules.credit(n)
print("Day 5")
n=int(input())
l=[-4,-3,1,6,-7,0,9,-1,5]
day5assignmentmodules.table(n)
day5assignmentmodules.count(l)
print("Day 6")
l=["1",2,3,"Hi",1.2,"hello",3.2]
day6assignmentmodules.count(l)
q=True
day6assignmentmodules.cont(q)
print("Day 7")
scorecard={
  'sakthi':{'class' :11,
  'subject':{'science':99, 'maths':70,'social':80}},
  'kanth':{'class' :11,
  'subject':{'science':90, 'maths':80,'social':80}},
  'kav':{'class' :11,
  'subject':{'science':80, 'maths':80,'social':80}},
  'john':{'class' :11,
  'subject':{'science':95, 'maths':85,'social':70}},
  'kant':{'class' :11,
  'subject':{'science':97, 'maths':90,'social':75}}}
day7assignmentmodules.stud(scorecard)
print("Day 8")
s=input()
day8assignmentmodules.sumofdigits(s)
s=input()
day8assignmentmodules.ispalindrome(s)
day8assignmentmodules.binary('10011')