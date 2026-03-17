def pal(s):
    f=0
    b=len(s)-1
    while f<b:
        if s[f]!=s[b]:
            return len(s)
        f+=1
        b-=1
    f=0
    b=len(s)-2
    while f<b:
        if s[f]!=s[b]:
            return len(s)-1
        f+=1
        b-=1
    return -1
s=input()
print(pal(s))
