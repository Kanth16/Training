def phno(string):
    a,b=[],[]
    for i in string:
        if i.isdigit():
            a.append(i)
        else:
            b.append(i)
    if len(a) !=10:
        b.reverse()
        n=10-len(a)
        n="".join(b[:n])
        a.append(n)
    a="".join(a)
    print(a)
    return a
#phno("abc99ef67d8992")
#phno("as9867dfgf5432ed1")