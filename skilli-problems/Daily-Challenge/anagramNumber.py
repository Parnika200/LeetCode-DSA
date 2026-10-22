def fun(n1,n2):
    s=str(n1)
    s2=str(n2)
    if sorted(s)==sorted(s2):
        return True
    else:
        return False

r=fun(111,32)
print(r)