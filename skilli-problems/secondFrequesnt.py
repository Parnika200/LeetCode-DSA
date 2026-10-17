n=[1,2,3,3,4,4,4]
d={}

for i in n:
    d[i]=d.get(i,0)+1
print(d) #{1: 1, 2: 1, 3: 2, 4: 3}
max=max(d.values())
s=0
for i in d:
    if d[i]<max and d[i]>s:
        s=i

print(s)