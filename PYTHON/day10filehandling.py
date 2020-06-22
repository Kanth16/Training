with open("day9.py","r") as d9:
  s=d9.readlines()
  for i in s:
    if "def" in i:
      s1=i[3:]
      s1=s1.split("(")[0]
      print(s1)