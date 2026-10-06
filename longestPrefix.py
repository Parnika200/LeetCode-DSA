str=["flower","fly","flow"]

def pref(str):
    prefix=str[0]
    for i in str:
       
        while not i.startswith(prefix):
            prefix=prefix[:-1]
    return prefix

res=pref(str)
print(res)