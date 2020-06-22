def cases(s):
  count1=count2=0
  for i in s:
    if(i.islower()):
      count1=count1+1
    else:
      count2=count2+1
  print("Lower:",count1,"\nUpper:",count2)