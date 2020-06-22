import requests
def get_method(url):
  resp=requests.get(url,verify=False)
  if resp.status_code in [200,200]:
    return (resp.content)
def write_method(filename,data):
  with open(filename,'wb') as wo:
    wo.write(data)
    return True
  return False
def get_values(filename):
  a=[]
  with open (filename,'r',encoding="UTF-8") as ro:
    s=ro.readlines()
    for i in range(len(s)):
      if i >= 125 and i <= 129:
        s[i]=s[i].split("<li>")[1]
        a.append(s[i].split("</li>")[0])
  print(a)
data=get_method("https://en.wikipedia.org/wiki/Python_(programming_language)")
status=write_method("C:\\Users\\k.a.ramasubramanian\\Desktop\\Training\\PY\\data.html",data)
if status:
  print(True)
else:
  print(False)
get_values("C:\\Users\\k.a.ramasubramanian\\Desktop\\Training\\PY\\data.html")