d={}
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
for i,j in scorecard.items():
  for a,b in j.items():
    if(isinstance(b,dict)):
      c=b.values()
      d[i]=sum(c)/3
print(d)
print(max(d,key=d.get))