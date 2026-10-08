num=14
# reduce num to 0, return steps needed to do so
#14 - 7 - 6- 3 -2-1 -0

def fun(num):
    c=0
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        while num!=0:
            if num%2!=0:
                num-=1
                c+=1
            else:
                num=num//2
                c+=1
    return c

a=fun(num)
print(a)