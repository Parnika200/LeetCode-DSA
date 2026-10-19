s="paper"
t="title"
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s.find(s[i]) != t.find(t[i]):
            return False

    return True

r=isIsomorphic(s,t)
print(r)