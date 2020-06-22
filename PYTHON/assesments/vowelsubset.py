def vowel(word):
        for i in word:
            if i in ["a","e","i","o","u"]:
                l=word.split(i)
                max_l=max(l,key=len)
                word=max_l
        return len(word)
word=input("Enter the word \n")
print(vowel(word))