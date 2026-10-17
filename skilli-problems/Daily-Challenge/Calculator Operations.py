n1=int(input("enter number"))
n2=int(input("enter number"))
op=input("enter operator")

def fun(n1,n2,op):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
            return n1*n2
    elif op=='/':
        if n2==0:
            return "devision by zero"
        return round(n1/n2,2)
    elif op=='//':
            
            return n1//n2
    elif op=='**':
         return n1**n2
    else:
         return "invalid operator"

res=fun(n1,n2,op)
print(res)