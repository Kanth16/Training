m={'stud1': {'name': 'student1', 'marks': [99, 44, 88]}, 'stud2': {'name': 'student2', 'marks': [88, 66, 88]}}
sampleDict = {  
'emp1': {'name': 'Jhon', 'salary': 7500},  
'emp2': {'name': 'Emma', 'salary': 8000},  
'emp3': {'name': 'Brad', 'salary': 6500}  
}
sampleDict['emp4']={'name':'kan','salary':10000}
sampleDict['emp2']['salary']=10000
print(sampleDict)
for i,j in m.items():
  print(i,j)
for i,j in m.items():
  for a,b in j.items():
    print(a,b)
for i, j in m.items():  
  for a,b in j.items():  
    if isinstance(m[i][a],list):  
      print("Total mark scored by "+i+" is "+str(sum(m[i][a])))
for i, j in m.items():  
  for a,b in j.items():  
    if a == 'marks':  
      print("Totak marks scored by - "+i+" is "+str(sum(b)))