def spelnum(spell):
    num=0
    ones={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
    tens={"ten":1,"twenty":2,"thirty":3,"forty":4,"fifty":5,"sixty":6,"seventy":7,"eighty":8,"ninety":9}
    hundreds={"hundred":2}
    l=spell.split(" ")
    for i in range(len(l)-1,-1,-1):
        if l[i] in ones.keys():
            num=ones[l[i]]
        elif l[i] in tens.keys():
            num=num+tens[l[i]]*10
        elif l[i] in hundreds.keys():
          num=num+(ones[l[i-1]]*(10**(hundreds[l[i]])))
          return num
    return num
def calc(spell):
    num=spelnum(spell)
    if num %2 !=0:
        for i in range(num,0,-1):
            print(i,end=",")
    else:
        for i in range(num,0,-2):
            print(i,end=",")
spell=input()
calc(spell)