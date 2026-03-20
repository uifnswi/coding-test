t=int(input())
for _ in range(t):
    tf=True
    arr=[]
    vps=list(input())
  
    for i in vps:
        if i=="(":
            arr.append(i)
        else:
            if len(arr)!=0 and arr[-1]=="(":
                arr.pop()
            else:
                tf=False
                arr.append(0)
                
    if len(arr)==0:tf=True
    else:tf=False
    if tf==True:print("YES")
    else:print("NO")

    