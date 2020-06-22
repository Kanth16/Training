def leapyear(year):
    count=0
    for i in range(1970,year+1):
        if i%4==0:
            count=count+1
    return count
def datecal(year):
    tl=leapyear(year)
    tm=(year-1970)*12
    td=tm*365
    th=td*24
    tmin=th*60
    tsec=tmin*60
    print("Total leap years:",tl,"years")
    print("Total Months    :",tm,"months")
    print("Total Days      :",td,"days")
    print("Total Hours     :",th,"hours")
    print("Total Minutes   :",tmin,"minutes")
    print("Total Seconds   :",tsec,"seconds")
year=int(input("Enter year > 1970"))
datecal(year)