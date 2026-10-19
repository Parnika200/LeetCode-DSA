str="1234"

def fun(str):
    n=""
    largest=0
    for i in str:
        n+=i
        if int(n[-1])%2!=0:
            if int(n)>largest:
                largest=int(n)
    if largest==0:
        return ""
    return largest

r=fun(str)
print(r)