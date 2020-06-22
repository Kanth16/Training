'''
def numpal(num):
    n=len(num)
    for i,j in zip(range(0,n),range(n-1,0,-1)):
        if(num[i]!=num[j]):
            return False
    return True
num=input()
print(numpal(num))
'''

def numpal(num,n,m):
    if(n==m): return True
    if num[n]!=num[m]: return False
    if n>m:return True
    else: return numpal(num,n+1,m-1)
num=input()
print(numpal(num,0,len(num)-1))