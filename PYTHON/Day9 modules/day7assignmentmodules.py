def stud(scorecard):
  d={}
  for i,j in scorecard.items():
    for a,b in j.items():
      if(isinstance(b,dict)):
        c=b.values()
        d[i]=sum(c)/3
  print(d)
  print(max(d,key=d.get))