str="hello bye hola"

def fun(str):
    words=str.split()
    return words[-1]

res=fun(str)
print(res)