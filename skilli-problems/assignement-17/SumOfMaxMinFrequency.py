n=[1,2,3,3,4,5,5,3]
d={}
for i in n:
    d[i]=d.get(i,0)+1

m=max(d.values())
mi=min(d.values())
print(m+mi)