s = """Python is often described as a "batteries included" language due to its comprehensive standard library.[29]"""
l=[]
l=s.split("\"")[1]
print(l)
name="Kanthimathinathan Ramasubramanian"
print(name.count("a"))
print(name.count("e"))
print(name.count("i"))
print(name.count("o"))
print(name.count("u"))
l=[]
l=name.split(" ")
print(l[1]+" "+l[0])
print(l[::-1])
print(" ".join(l[::-1]))