s1=input("enter string")
s2=input("enter string")

count={}

def fun(s1,s2):
    for c in s1:
        count[c]=count.get(c,0)+1

    for c in s2:
        if c not in count:
            return False
        count[c]-=1
        if count[c]<0:
            return False
    return True

f=fun(s1,s2)
print(f)