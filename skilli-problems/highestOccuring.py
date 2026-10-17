nums=[1,2,3,5,6,6,6]
d={}
for i in nums:
    d[i]=d.get(i,0)+1
print(max(d,key=d.get))